from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsOwnerOrEditorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True

        if request.method in permissions.SAFE_METHODS:
            return request.user.groups.filter(name='Editor').exists()

        return False