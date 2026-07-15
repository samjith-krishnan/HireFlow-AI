from rest_framework.permissions import BasePermission

from apps.common.choices import UserRole


class IsOwnerOrHR(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                UserRole.OWNER,
                UserRole.HR,
            ]
        )