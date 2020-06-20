from rest_framework import viewsets

from .models import  Unicorn 
from .serializers  import UnicornSerializer

class UnicornViewSet(viewsets.ModelViewSet):
    queryset = Unicorn.objects.all()
    serializers_class = UnicornSerializer

    