from django.urls import path, include
from rest_framework import routers
from adopet.views import TutorViewSet

router = routers.DefaultRouter()
router.register("tutors", TutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]