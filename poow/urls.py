
from django.conf.urls import url, include

from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from poow.views import PooSessionViewSet

router = routers.DefaultRouter()
router.register(r'poosession', PooSessionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]