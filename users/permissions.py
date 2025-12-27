from rest_framework.permissions import BasePermission

class IsDeaconOrAbove(BasePermission):
    """
    Pastor, Priest, Deacon
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(
                name__in=["Pastor", "Priest", "Deacon"]
            ).exists()
        )


class IsPastorOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Pastor").exists()
        )
