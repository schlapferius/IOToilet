
from rest_framework import serializers

from poow.models import Poo


class PooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poo
        fields = '__all__'