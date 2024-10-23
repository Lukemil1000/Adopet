from rest_framework import permissions, viewsets, mixins
from rest_framework import views
from adopet.models import Tutor, Shelter, Pet, Adoption
from adopet.serializers import TutorSerializer, ShelterSerializer, PetSerializer, AdoptionSerializer, LoginSerializer
from adopet.permissions import IsPetShelterPermission
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework import status

class TutorViewSet(viewsets.ModelViewSet):
    """Endpoint para o modelo de Tutor"""

    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class ShelterViewSet(viewsets.ModelViewSet):
    """Endpoint para o modelo de Abrigo"""

    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class PetViewSet(viewsets.ModelViewSet):
    """Endpoint para o modelo de Pet"""

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filterset_fields = ['adopted', "shelter"]
    permission_classes = (IsPetShelterPermission,)

class AdoptionViewSet(viewsets.ModelViewSet):

    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer
    http_method_names = ["get", "post", "delete", "head", "options"]

class LoginView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    def get_serializer(self, *args, **kwargs):
        return LoginSerializer(*args, **kwargs)

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
    
class LogoutView(views.APIView):

    def get(self, request):
        logout(request)
        return Response(None, status=status.HTTP_200_OK)