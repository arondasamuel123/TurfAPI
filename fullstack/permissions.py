from rest_framework.permissions import BasePermission

class TurfOwner(BasePermission):
    
    def has_permission(self, request, view):
        if(request.user.role_type=='TO'):
            return request.user
        
class TurfUser(BasePermission):
    def has_permission(self, request, view):
        if(request.user.role_type=='TU'):
            
            return request.user