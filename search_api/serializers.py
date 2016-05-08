# -*- coding: utf-8 -*-

import serpy


class CitySerializer(serpy.Serializer):
    id = serpy.IntField()
    name = serpy.Field()


class AutoCompleteList(serpy.Serializer):
    id = serpy.IntField()
    name = serpy.Field()
    kind = serpy.MethodField()

    def get_kind(self, obj):
        return obj.kind


class HotelSerializer(serpy.Serializer):
    id = serpy.IntField()
    name = serpy.Field()
    city = CitySerializer()


class AvailabilitySerializer(serpy.Serializer):
    id = serpy.IntField()
    date = serpy.MethodField()
    available = serpy.BoolField()
    hotel = HotelSerializer()

    def get_date(self, obj):
        return obj.date.isoformat()