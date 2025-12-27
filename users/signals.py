from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(post_migrate)
def create_church_groups(sender, **kwargs):
    groups = [
        "Pastor",
        "Priest",
        "Deacon",
        "Secretary",
        "Accountant",
        "Admin Staff",
        "Worship Team",
        "Teachers",
        "Ushers",
        "Members",
    ]

    for name in groups:
        Group.objects.get_or_create(name=name)
