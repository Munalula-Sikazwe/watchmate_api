from rest_framework import permissions
from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):
    ## check if the user is a director.
    def has_permission(self, request, view):
        return request.user.user_role == 'customer'


class ReviewPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in  permissions.SAFE_METHODS:
            return True
        else:
            return obj.reviewer == request.user
