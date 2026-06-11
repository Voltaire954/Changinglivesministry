from django.db import models


class LiveStream(models.Model):
    title = models.CharField(max_length=255, default="Live Service")

    stream_url = models.URLField(
        help_text="Facebook Live, YouTube Live, Vimeo embed URL"
    )

    is_active = models.BooleanField(default=False)

    platform = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="facebook, youtube, vimeo"
    )

    started_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
