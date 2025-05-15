from rest_framework.permissions import BasePermission

class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'sistema', None) == 'P' 
    
class IsDisciplina(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'sistema', None) == 'D'

class IsAmbiente(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'sistema', None) == 'A'

class IsGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'sistema', None) in ['P', 'D', 'A']
