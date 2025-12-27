from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

MEDIA_TYPE_CHOICES = [
    ("image", "Image"),
    ("video", "Video"),
    ("document", "Document"),
]


class Media(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="uploads/%Y/%m/%d/")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
