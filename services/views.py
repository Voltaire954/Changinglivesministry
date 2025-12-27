from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsDeaconOrAbove
from services.services import create_service, update_service, delete_service
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAuthenticated()]
        return [IsDeaconOrAbove()]

    def perform_create(self, serializer):
        create_service(
            user=self.request.user,
            data=serializer.validated_data
        )

    def perform_update(self, serializer):
        update_service(
            user=self.request.user,
            instance=self.get_object(),
            data=serializer.validated_data
        )

    def perform_destroy(self, instance):
        delete_service(
            user=self.request.user,
            instance=instance
        )
