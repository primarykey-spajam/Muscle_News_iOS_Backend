
# coding: utf-8

from rest_framework import routers
from .views import MuscleViewSet


router = routers.DefaultRouter()
router.register(r'muscles', MuscleViewSet)
