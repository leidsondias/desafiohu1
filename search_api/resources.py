# -*- coding: utf-8 -*-

from flask import request
from flask_restful import (Api, Resource)
from flask_restful import reqparse

from .models import (Hotel, City, Availability)
from .serializers import AutoCompleteList, AvailabilitySerializer


api = Api()


class AutoCompleteListResource(Resource):
    def get(self):
        query = request.args.get('query')
        limit = int(request.args.get('limit', 0))
        offset = int(request.args.get('offset', 10))
        obj_list = []
        if query:
            for model in (Hotel, City):
                object = model.query.filter(model.name.like(query+'%')) \
                    .slice(limit, offset)
                obj_list.extend(object)
        else:
            # @TODO ERRO
            pass

        serializer = AutoCompleteList(obj_list, many=True)

        return serializer.data


class SearchResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('kind')
    parser.add_argument('id')
    parser.add_argument('start_date')
    parser.add_argument('end_date')

    def post(self):
        params = self.parser.parse_args()
        kind = params.get('kind')
        _id = params['id']
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        filters = {'available': True}
        date_filter = ''

        if start_date:
            date_filter = Availability.date.between(start_date, end_date)
            filters.pop('available')

        if kind == 'city':
            query = Availability.query.filter_by(**filters). \
                from_self(). \
                join(Availability.hotel).filter_by(city_id=_id). \
                filter(date_filter)
        else:
            filters.update({"hotel_id": _id})
            query = Availability.query.filter_by(**filters). \
                filter(date_filter)

        serializer = AvailabilitySerializer(query, many=True)

        return serializer.data


api.add_resource(AutoCompleteListResource, '/list')
api.add_resource(SearchResource, '/search')

