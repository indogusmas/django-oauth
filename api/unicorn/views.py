from django.shortcuts import render
from rest_framework import viewsets

from .models import Unicorn
from .serializers import UnicornSerializer

# Create your views here.
class UnicornViewSet(viewsets.ModelViewSet):
    queryset = Unicorn.objects.all()
    serializer_class = UnicornSerializer
    