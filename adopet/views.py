from rest_framework import permissions, viewsets, mixins
from adopet.models import Tutor, Shelter, Pet, Adoption
from adopet.serializers import TutorSerializer, ShelterSerializer, PetSerializer, AdoptionSerializer

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

class AdoptionViewSet(viewsets.ModelViewSet):

    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer
    http_method_names = ["get", "post", "delete", "head", "options"]