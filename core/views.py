from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Image
from .serializers import ImageSerializer


class SearchImagesView(APIView):

    def get(self, request, *args, **kwargs):
        search_key = kwargs.get('searchTerm')
        images = Image.objects.filter(
            Q(author__icontains=search_key) |
            Q(camera__icontains=search_key) |
            Q(tags__icontains=search_key)
        )

        serializer = ImageSerializer(images, many=True)

        return Response(serializer.data)
