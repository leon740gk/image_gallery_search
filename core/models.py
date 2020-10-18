from djongo import models


class Image(models.Model):

    own_id = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    cropped_picture = models.URLField()
    full_picture = models.URLField()
