# -*- coding: utf-8 -*-
import datetime
import unittest
import urllib
import json

from search_api import app, db
from search_api.models import (City, Hotel, Availability)


class TestSearchApi(unittest.TestCase):
    def _import_city(self, _city):
        city = City.query.filter_by(name=_city).first()
        if city:
            return city.id
        else:
            city = City(_city)
            db.session.add(city)
            db.session.commit()
            city = City.query.filter_by(name=_city).first()
            return city.id

    def setUp(self):
        app.config.from_object('search_api.settings_test')
        db.create_all()
        self.app = app.test_client()

        response = urllib.urlopen('artefatos/hoteis_test.txt')

        for line in response.readlines():
            _id, _city, name = str(line.strip()).split(',')

            city = self._import_city(_city.decode('utf-8'))

            hotel = Hotel(name.decode('utf-8'), city)
            db.session.add(hotel)

        response = urllib.urlopen('artefatos/disp_test.txt')

        for line in response.readlines():
            hotel_id, date, available = str(line.strip()).split(',')
            date = datetime.datetime.strptime(date, '%d/%m/%Y')
            availability = Availability(hotel_id, date.date(), available)
            db.session.add(availability)

        db.session.commit()

    def tearDown(self):
        # @TODO: Remover banco de teste criado
        db.drop_all()
        db.session.close()

    def test_create_city(self):
        u"""
        Teste de criação de cidade
        """
        city = City(name='Campina Grande')
        db.session.add(city)
        db.session.commit()
        city = City.query.filter_by(name='Campina Grande').first()
        self.assertEquals('Campina Grande', city.name)

    def test_get_city(self):
        u"""
        Teste de retorno de cidade por <id>
        """
        city = City.query.get(1)
        self.assertEqual('Macae', city.name)

    def test_create_hotel(self):
        u"""
        Teste de criação de hotel
        """
        hotel = Hotel(name='Meu Hotel', city_id=1)
        db.session.add(hotel)
        db.session.commit()
        hotel = Hotel.query.filter_by(name='Meu Hotel').first()
        self.assertTrue('Meu Hotel', hotel.name)

    def test_get_hotel_id(self):
        u"""
        Teste de retorno de hotel por <id>
        """
        hotel = Hotel.query.get(1)
        self.assertEqual('Seyhan', hotel.name)

    def test_get_hotel_city_id(self):
        u"""
        Teste de retorno de hotel por <cidade>
        """
        hotels = Hotel.query.filter_by(city_id=1).all()
        self.assertTrue(hotels)

    def test_create_availability(self):
        u"""
        Teste de criação de uma disponibilidade
        """
        availability = Availability(hotel_id=1, date=datetime.datetime(2015,05,14), available=1)
        db.session.add(availability)
        db.session.commit()
        availabilities = Availability.query.all()
        self.assertTrue(availabilities)

    def test_get_availability_id(self):
        u"""
        Teste de retorno de disponibilidade por <id>
        """
        availability = Availability.query.get(1)
        self.assertTrue(availability)

    def test_api_get_auto_complete(self):
        u"""
        Teste de retorno do autocomplete
        """
        # Teste get de uma cidade existente
        response = self.app.get('/list?query=Macae')
        data = json.loads(response.data)
        self.assertEquals('Macae', data[0].get('name'))

        # Teste get de uma cidade ineexistente
        response = self.app.get('/list?query=Campina Grande')
        data = json.loads(response.data)

        self.assertFalse(data)

    def test_api_get_availability_search(self):
        u"""
        Teste de retorno de disponibilidade por <hotel>, <city> e/ou <date>
        """

        # Teste search city <kind:city>, <date:true>
        params = {"start_date": '2015-05-04', "end_date":'2015-05-06', "id": 1, "kind": "city"}
        response = self.app.post('search', data=params)
        data = json.loads(response.data)
        self.assertEquals(2, len(data))

        # >>>>  Intervalo com algum dia ocupado de ambos hoteis portanto indisponível
        params = {"start_date": '2015-05-10', "end_date":'2015-05-16', "id": 1, "kind": "city"}
        response = self.app.post('search', data=params)
        data = json.loads(response.data)
        self.assertFalse(data)

        # Teste search city <kind:city>, <date:false>
        params = {"id": 1, "kind": "city"}
        response = self.app.post('search', data=params)
        data = json.loads(response.data)
        self.assertEquals(2, len(data))

        # Teste search hotel <kind:hotel>, <date:true>
        params = {"start_date": '2015-05-04', "end_date":'2015-05-06', "id": 1, "kind": "hotel"}
        response = self.app.post('search', data=params)
        data = json.loads(response.data)
        self.assertEquals('Seyhan', data[0].get('hotel').get('name'))

        # >>>> Intervalo com data indisponível para esse hotel
        params = {"start_date": '2015-05-07', "end_date":'2015-05-09', "id": 1, "kind": "hotel"}
        response = self.app.post('search', data=params)
        data = json.loads(response.data)
        self.assertFalse(data)

        # Teste search hotel <kind:hotel>, <date:false>
        params = {"id": 1, "kind": "hotel"}
        response = self.app.post('search', data=params)
        data = json.loads(response.data)
        self.assertEquals('Seyhan', data[0].get('hotel').get('name'))




