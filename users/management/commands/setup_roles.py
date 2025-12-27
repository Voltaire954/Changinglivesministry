from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

ROLE_DEFINITIONS = {
    "Pastor": "__all__",
    "Priest": "__all__",

    "Deacon": [
        "add_user", "change_user", "view_user",
        "add_service", "change_service", "view_service",
    ],

    "Admin": "__all__",

    "Secretary": [
        "add_user", "change_user", "view_user",
    ],

    "Accountant": [
        "view_transaction", "add_transaction",
    ],

    "Worship Team": [
        "view_service",
    ],

    "Teachers": [
        "view_service",
    ],

    "Ushers": [
        "view_service",
    ],

    "Member": [
        "view_service",
    ],
}

class Command(BaseCommand):
    help = "Create church roles and assign permissions"

    def handle(self, *args, **kwargs):
        all_permissions = Permission.objects.all()

        for role, perms in ROLE_DEFINITIONS.items():
            group, created = Group.objects.get_or_create(name=role)

            if perms == "__all__":
                group.permissions.set(all_permissions)
            else:
                permissions = Permission.objects.filter(codename__in=perms)
                group.permissions.set(permissions)

            group.save()

            status = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{status} role: {role}"))
