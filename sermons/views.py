from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Sermon
from .serializers import SermonSerializer

class SermonViewSet(ModelViewSet):
    queryset = Sermon.objects.all().order_by("-preached_on")
    serializer_class = SermonSerializer
# Create your views here.
