from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return(
            request.method in SAFE_METHODS and
            request.user.is_authenticated
        )

class PostPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return(
                request.user.id == obj.owner.id and
                request.user.is_authenticated
            )