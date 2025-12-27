from django.core.exceptions import PermissionDenied
from services.models import Service
from audit.services import log_action


def create_service(*, user, data):
    if not user.has_perm("services.add_service"):
        raise PermissionDenied("You are not allowed to create services")

    service = Service.objects.create(**data)

    log_action(
        user=user,
        action="create",
        instance=service,
        message="Service created",
    )

    return service


def update_service(*, user, instance, data):
    if not user.has_perm("services.change_service"):
        raise PermissionDenied("You are not allowed to update services")

    for field, value in data.items():
        setattr(instance, field, value)
    instance.save()

    log_action(
        user=user,
        action="update",
        instance=instance,
        message="Service updated",
    )

    return instance


def delete_service(*, user, instance):
    if not user.has_perm("services.delete_service"):
        raise PermissionDenied("You are not allowed to delete services")

    log_action(
        user=user,
        action="delete",
        instance=instance,
        message="Service deleted",
    )

    instance.delete()
