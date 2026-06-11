from django.db import models


class Sermon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    speaker = models.CharField(max_length=255, blank=True)
    preached_on = models.DateField()

    video_url = models.URLField(
        blank=True,
        null=True,
        help_text="YouTube, Facebook Live, Vimeo, etc."
    )

    thumbnail = models.ImageField(
        upload_to="sermon_thumbnails/",
        blank=True,
        null=True
    )

    live_url = models.URLField(
        blank=True,
        null=True,
        help_text="YouTube Live, Facebook Live, Vimeo, or embed link"
    )

    def __str__(self):
        return self.title
