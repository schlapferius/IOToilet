
from django.conf.urls import url, include

from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from poow.viewset import PooSessionViewSet


router_poo = routers.SimpleRouter(trailing_slash=False)
router_poo.register(r'', PooSessionViewSet, base_name='poos')

urlpatterns = [
    url(r'',
        include(router_poo.urls)
        ),
]