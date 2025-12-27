from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from audit.services import log_action

User = get_user_model()


def create_user(*, actor, data):
    if not actor.has_perm("auth.add_user"):
        raise PermissionDenied("You cannot create users")

    user = User.objects.create(**data)

    log_action(
        user=actor,
        action="create",
        instance=user,
        message="User account created",
    )

    return user


def update_user(*, actor, instance, data):
    if not actor.has_perm("auth.change_user"):
        raise PermissionDenied("You cannot update users")

    for field, value in data.items():
        setattr(instance, field, value)
    instance.save()

    log_action(
        user=actor,
        action="update",
        instance=instance,
        message="User account updated",
        metadata={"fields": list(data.keys())},
    )

    return instance
