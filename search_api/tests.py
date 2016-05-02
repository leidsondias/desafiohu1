# -*- coding: utf-8 -*-

import unittest
import random
import os

from datetime import datetime

from search_api import app, db
from search_api.models import (City, Hotel, Availability)


class TestSearchApi(unittest.TestCase):
    def setUp(self):
        app.config.from_object('search_api.settings_test')
        db.create_all()

    def tearDown(self):
        # @TODO: Remover banco de teste criado
        # db.drop_all()
        # db.session.close()
        pass

    def test_create_city(self):
        u"""
        Teste de criação de cidade
        """
        city = City(name='Rio de Janeiro')
        db.session.add(city)
        db.session.commit()
        cities = City.query.all()
        self.assertTrue(cities)

    def test_get_city(self):
        u"""
        Teste de retorno de cidade por <id>
        """
        city = City.query.get(1)
        self.assertEqual('Rio de Janeiro', city.name)

    def test_create_hotel(self):
        u"""
        Teste de criação de hotel
        """
        hotel = Hotel(name='Meu Hotel', city_id=1)
        db.session.add(hotel)
        db.session.commit()
        hotels = Hotel.query.all()
        self.assertTrue(hotels)

    def test_get_hotel_id(self):
        u"""
        Teste de retorno de hotel por <id>
        """
        hotel = Hotel.query.get(1)
        self.assertEqual('Meu Hotel', hotel.name)

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
        availability = Availability(hotel_id=1, date=datetime(2015,05,04), available=1)
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

    def test_get_availability_search(self):
        u"""
        Teste de retorno de disponibilidade por <hotel>
        """
        is_ok = True
        start_date = '2015-05-04'
        end_date = '2015-05-06'
        availability = Availability.query.filter_by(hotel_id=1)
        if not availability:
            is_ok = False

        availability = Availability.query.filter(Availability.date.between(start_date, end_date))
        if not availability:
            is_ok = False

