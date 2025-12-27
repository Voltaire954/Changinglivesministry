from django.core.exceptions import PermissionDenied

def create_member(*, user, data):
    if not user.has_perm("members.add_member"):
        raise PermissionDenied("You are not allowed to add members")

    # business logic
    return Member.objects.create(**data)
