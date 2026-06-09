from django.db import models


class Sermon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    speaker = models.CharField(max_length=255, blank=True)
    preached_on = models.DateField()

    thumbnail = models.ImageField(
        upload_to="sermon_thumbnails/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
