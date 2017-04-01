

from rest_framework import  viewsets
# Create your views here.

# ViewSets define the view behavior.
from poow.models import Poo
from poow.serializers import PooSerializer


class PooSessionViewSet(viewsets.ModelViewSet):
    queryset = Poo.objects.all()
    serializer_class = PooSerializer