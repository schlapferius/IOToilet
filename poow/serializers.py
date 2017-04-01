
from rest_framework import serializers

from poow.models import Poo, Measure



class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = (
            'timestamp',
            'sensor_fr',
            'sensor_fl',
            'sensor_br',
            'sensor_bl',
        )


class PooSerializer(serializers.ModelSerializer):
    measure_set = MeasureSerializer(
        many=True
    )

    class Meta:
        model = Poo
        fields = (
            'uuid',
            'measure_set'
        )
