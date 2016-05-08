#!/usr/bin/env python

# -*- coding: utf-8 -*-
import os

from flask_script import Manager, prompt_bool

from search_api import app, db
from search_api.models import City

manager = Manager(app)


@manager.command
def test():
    import unittest
    testmodules = [
        'search_api.tests',
    ]

    suite = unittest.TestSuite()

    for t in testmodules:
        try:
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    unittest.TextTestRunner().run(suite)


@manager.command
def create_db():
    db.create_all()


@manager.command
def drop_db():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()


@manager.command
def recreate_db():
    drop_db()
    create_db()


@manager.command
def load_db():
    import urllib, datetime
    from search_api.models import (Hotel, Availability)

    response = urllib.urlopen('artefatos/hoteis.txt')

    for line in response.readlines():
        _id, _city, name = str(line.strip()).split(',')

        city = _import_city(_city.decode('utf-8'))

        hotel = Hotel(name.decode('utf-8'), city)
        db.session.add(hotel)

    response = urllib.urlopen('artefatos/disp.txt')

    for line in response.readlines():
        hotel_id, date, available = str(line.strip()).split(',')
        date = datetime.datetime.strptime(date, '%d/%m/%Y')
        availability = Availability(hotel_id, date.date(), available)
        db.session.add(availability)

    db.session.commit()


def _import_city(_city):
    city = City.query.filter_by(name=_city).first()
    if city:
        return city.id
    else:
        city = City(_city)
        db.session.add(city)
        db.session.commit()
        city = City.query.filter_by(name=_city).first()
        return city.id


if __name__ == '__main__':
    manager.run()
