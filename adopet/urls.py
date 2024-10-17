from django.urls import path, include
from rest_framework import routers
from adopet.views import TutorViewSet, ShelterViewSet, PetViewSet, AdoptionViewSet, LoginView, LogoutView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register
router.register("tutors", TutorViewSet)
router.register("shelters", ShelterViewSet)
router.register("pets", PetViewSet)
router.register("adoptions", AdoptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]