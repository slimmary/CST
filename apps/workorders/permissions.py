from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' or request.user.is_staff:
            return True
        return obj.car.client == request.user


class ReadOnlyMethod(permissions.BasePermission):
    def has_permission(self, request, view):
        read_only_methods = ('GET', 'OPTIONS', 'HEAD')
        return request.method in read_only_methods
