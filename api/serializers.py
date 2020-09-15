from rest_framework import serializers
from sokna.models import SoknaRequest
from daira.models import Mol7aka


class SoknaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoknaRequest
        fields = [
            'id',
            'CIN',
            'firstname',
            'lastname',
            'born_d',
            'born_m',
            'born_y',
            'born_no_d_m',
            'gender',
            'phone',
            'address',
            'mol7aka',
            'photo_1',
            'photo_2',
            'get_status',
            'notes'
        ]
        read_only_fields = ['status', 'notes']


class Mol7akaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mol7aka
        fields = ['id', 'name', 'name_in_arabic']
