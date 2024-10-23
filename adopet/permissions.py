from rest_framework import permissions
from adopet.models import Shelter

class IsPetShelterPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.is_authenticated and request.user.user_type == "shelter":
                shelter = request.data.get("shelter")
                instance = Shelter.objects.get(pk=shelter)
                return instance == request.user.shelter
            return False  
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.user_type == "shelter":
            return obj.shelter == request.user.shelter
        return False
