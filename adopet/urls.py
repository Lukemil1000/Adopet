from django.urls import path, include
from rest_framework import routers
from adopet.views import TutorViewSet, ShelterViewSet, PetViewSet

router = routers.DefaultRouter()
router.register("tutors", TutorViewSet)
router.register("shelters", ShelterViewSet)
router.register("pets", PetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]