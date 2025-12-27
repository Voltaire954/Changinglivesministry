from audit.models import AuditLog

def log_action(
    *,
    user,
    action,
    instance,
    message="",
    metadata=None,
):
    AuditLog.objects.create(
        user=user,
        action=action,
        model=instance.__class__.__name__,
        object_id=str(instance.pk),
        message=message,
        metadata=metadata or {},
    )
