from django.test import TestCase

# Create your tests here.
from iot.poow.models import Poo, Measure


class PooTestCase(TestCase):
    def setUp(self):

        p = Poo.objects.create(uuid='12345')
        for i in range(10):
            Measure.objects.create(
                poo=p,
                timestamp=i * 0.1,
                sensor_fr=i * 0.1,
                sensor_fl=i * 0.1,
                sensor_br=i * 0.1,
                sensor_bl=i * 0.1,
            )

    def test_shit_happend(self):
        pass
