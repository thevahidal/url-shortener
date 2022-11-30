
from rest_framework import serializers

from .models import ShortenedURL


class ShortenURLSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    
    class Meta:
        model = ShortenedURL
        fields = ['url', 'slug']