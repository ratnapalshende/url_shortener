from rest_framework import serializers
from .models import ShortenedURL

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['id', 'url', 'shortCode', 'createdAt', 'updatedAt', 'accessCount']
        read_only_fields = ['shortCode', 'createdAt', 'updatedAt', 'accessCount']
