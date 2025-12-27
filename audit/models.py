from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=50)
    model = models.CharField(max_length=100, blank=True)       # add this
    object_id = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)                      # add this
    metadata = models.JSONField(blank=True, default=dict)       # add this
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.model}"
