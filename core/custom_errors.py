from rest_framework import status
from rest_framework.exceptions import APIException


class TokenExpired(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = 'TOKEN_EXPIRED'
    default_detail = 'This toke expired.'
