from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now =True)

    class Meta:
        permissions = [
            ("manage_services", "Can manage services"),
            ("view_services", "Can view services"),
        ]
