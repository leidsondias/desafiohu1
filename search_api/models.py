# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    hotels = db.relationship('Hotel', backref='city',
                             lazy='dynamic')

    def __init__(self, name):
        self.name = name

    @property
    def kind(self):
        return 'city'


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    availabilities = db.relationship('Availability', backref='hotel',
                                     lazy='dynamic')

    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id

    def __repr__(self):
        return 'Hotel({name!r})'.format(name=self.name)

    @property
    def kind(self):
        return 'hotel'


class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
    available = db.Column(db.Boolean)

    def __init__(self, hotel_id, date, available):
        self.hotel_id = hotel_id
        self.date = date
        self.available = available
