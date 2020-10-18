import datetime
import json

import requests
from django.conf import settings
from rest_framework import status

from .models import Image
from .utils import CacheImageRedis
from .auth_token import get_new_token

class ImageManager:

    def __init__(self):
        self.token = get_new_token()
        self.url = settings.IMAGE_BASE_URL + '/images/'
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.cache_client = CacheImageRedis()

    def load_images_to_cache(self):
        raw_response = requests.get(url=self.url, headers=self.headers)
        if raw_response.status_code == status.HTTP_401_UNAUTHORIZED:
            self.token = get_new_token()
            raw_response = self.load_images_to_cache()

        response = json.loads(raw_response.text)
        picture_ids = [picture.get('id') for picture in response.get('pictures')]
        while response.get('hasMore'):
            raw_response = requests.get(
                url=self.url + f"?page={response.get('page') + 1}",
                headers=self.headers
            )
            response = json.loads(raw_response.text)
            picture_ids.extend([picture.get('id') for picture in response.get('pictures')])


        for id in picture_ids:
            raw_picture_details = requests.get(url=self.url + id, headers=self.headers)
            picture_details = json.loads(raw_picture_details.text)

            Image.objects.update_or_create(
                own_id=picture_details.get('id'),
                author=picture_details.get('author'),
                camera=picture_details.get('camera'),
                tags=picture_details.get('tags'),
                cropped_picture=picture_details.get('cropped_picture'),
                full_picture=picture_details.get('full_picture')
            )
