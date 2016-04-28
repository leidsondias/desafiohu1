# -*- coding: utf-8 -*-

from flask import Flask

from .resources import api
from .models import db

app = Flask(__name__)
app.config.from_object('search_api.settings')

api.init_app(app)
db.init_app(app)
