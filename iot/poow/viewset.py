

from rest_framework import  viewsets
# Create your views here.

# ViewSets define the view behavior.
from iot.poow.models import Poo
from iot.poow.serializers import PooSerializer



class PooSessionViewSet(viewsets.ModelViewSet):
    """ I like to shit, ain't you?        measure_set: 'timestamp', 'sensor_fr', 'sensor_fl', 'sensor_br', 'sensor_bl',

            ---
            response_serializer: PooSerializer
            responseMessages:
            - code: 200
              message: Ok
            """
    queryset = Poo.objects.all()
    serializer_class = PooSerializer
