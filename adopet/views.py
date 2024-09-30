from rest_framework import permissions, viewsets
from adopet.models import Tutor, Shelter, Pet
from adopet.serializers import TutorSerializer, ShelterSerializer, PetSerializer

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

    queryset = Pet.objects.filter(adopted=False)
    serializer_class = PetSerializer