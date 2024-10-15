from django.urls import path, include
from rest_framework import routers
from adopet.views import TutorViewSet, ShelterViewSet, PetViewSet, AdoptionViewSet, LoginView

router = routers.DefaultRouter()
router.register
router.register("tutors", TutorViewSet)
router.register("shelters", ShelterViewSet)
router.register("pets", PetViewSet)
router.register("adoptions", AdoptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
]