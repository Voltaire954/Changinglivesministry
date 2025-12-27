from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

from audit.services import log_action


@receiver(user_logged_in)
def audit_user_login(sender, request, user, **kwargs):
    log_action(
        user=user,
        action="login",
        instance=user,
        message="User logged in",
        metadata={
            "ip": request.META.get("REMOTE_ADDR"),
            "user_agent": request.META.get("HTTP_USER_AGENT"),
        },
    )


@receiver(user_logged_out)
def audit_user_logout(sender, request, user, **kwargs):
    log_action(
        user=user,
        action="logout",
        instance=user,
        message="User logged out",
        metadata={
            "ip": request.META.get("REMOTE_ADDR"),
        },
    )
