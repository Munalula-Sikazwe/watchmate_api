from rest_framework.permissions import BasePermission

class UserPermissions(BasePermission):
## check if the user is a director.
    def has_permission(self,request,view):
        return request.user.user_role == 'customer'