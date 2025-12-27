from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Donation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='USD')
    payment_method = models.CharField(max_length=50, default='PayPal')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount} {self.currency} - {self.status}"
