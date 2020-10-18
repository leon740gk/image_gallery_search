from celery.schedules import crontab
from celery.task import periodic_task
from django.conf import settings


@periodic_task(
    name='Refresh cache of images',
    run_every=crontab(
        minute=settings.CELERY_PERIODIC_TASK_MINUTES,
        hour=settings.CELERY_PERIODIC_TASK_HOURS
    ),
    ignore_result=False,
    soft_time_limit=240,
)
def refresh_cache():
    from .images_loader import ImageManager

    images_loader_client = ImageManager()
    images_loader_client.load_images_to_cache()
