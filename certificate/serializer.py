# coding: utf-8

from rest_framework import serializers
from .models import Certificate


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        depth = 1
        fields = ['id', 'name', 'text_1', 'text_2', 'date', 'text_3', 'time', 'logo']
