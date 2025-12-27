from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Media
from .serializers import MediaSerializer
from users.permissions import IsDeaconOrAbove  # optional custom permission

class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all().order_by("-uploaded_at")
    serializer_class = MediaSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAuthenticated()]
        return [IsDeaconOrAbove()]  # only Deacon+ can create/update/delete
