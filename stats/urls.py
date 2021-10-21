from django.db.models import base
from rest_framework import routers, urlpatterns
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ClickStatisticViewset

router = SimpleRouter()
router.register(r"click-statistic", ClickStatisticViewset,
                basename="ClickStatistic")

urlpatterns = [
    path("", include(router.urls)),
]
