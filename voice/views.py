# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import Muscle
from .serializer import MuscleSerializer


class MuscleViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MuscleSerializer
