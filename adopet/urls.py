from django.urls import path, include
from rest_framework import routers
from adopet.views import TutorViewSet, ShelterViewSet

router = routers.DefaultRouter()
router.register("tutors", TutorViewSet)
router.register("shelters", ShelterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]