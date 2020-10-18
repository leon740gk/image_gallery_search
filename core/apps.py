from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = _('core')

    def ready(self):
        from .images_loader import ImageManager

        images_loader_client = ImageManager()
        images_loader_client.load_images_to_cache()
