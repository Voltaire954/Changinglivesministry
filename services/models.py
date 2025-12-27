from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateField()

    class Meta:
        permissions = [
            ("manage_services", "Can manage services"),
            ("view_services", "Can view services"),
        ]
