from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):

    own_id = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    camera = serializers.CharField(max_length=255)
    tags = serializers.CharField(max_length=255)
    cropped_picture = serializers.URLField()
    full_picture = serializers.URLField()

    class Meta:
        model = Image
        fields = (
            'own_id',
            'author',
            'camera',
            'tags',
            'cropped_picture',
            'full_picture'
        )
