from rest_framework.permissions import BasePermission


class IsCurator(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Curator').exists():
            # Пользователь принадлежит к группе
            return True
        else:
            # Пользователь не принадлежит к группе
            return False
