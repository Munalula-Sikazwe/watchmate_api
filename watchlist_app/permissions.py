from rest_framework.permissions import BasePermission

class user_permissions(BasePermission):

    def has_permission(self,request,view):
        return request.user.user_role == 'director'