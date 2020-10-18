import json

import requests
from django.conf import settings


def get_new_token():
    url = settings.IMAGE_BASE_URL + '/auth'
    payload = {'apiKey': settings.API_KEY}
    raw_response = requests.post(url=url, json=payload)
    response = json.loads(raw_response.text)

    return response.get('token')
