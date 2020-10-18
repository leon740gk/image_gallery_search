from django.core.cache import cache


class CacheImageRedis:

    KEY_PREFIX = 'picture_cache'

    def __make_key(self, picture_id):
        key = f'{picture_id}'
        return key

    def get_from_redis(self, key):
        return cache.get(key)

    def set_in_redis(self, picture_id, picture_details):
        key = self.__make_key(picture_id)
        cache.set(key, picture_details, timeout=None)

    def get_all_keys(self):
        return cache.get('*')
