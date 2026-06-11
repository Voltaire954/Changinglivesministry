from rest_framework import generics
from .models import LiveStream
from .serializers import LiveStreamSerializer


class LiveStreamListView(generics.ListAPIView):
    queryset = LiveStream.objects.all()
    serializer_class = LiveStreamSerializer
