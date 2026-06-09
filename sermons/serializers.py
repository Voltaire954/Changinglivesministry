from rest_framework import serializers
from .models import Sermon
from media.serializers import MediaSerializer

class SermonSerializer(serializers.ModelSerializer):
    media_files = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = Sermon
        fields = "__all__"
