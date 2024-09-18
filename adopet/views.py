from rest_framework import permissions, viewsets
from adopet.models import Tutor
from adopet.serializers import TutorSerializer

class TutorViewSet(viewsets.ModelViewSet):
    """Endpoint para o modelo de Tutor"""

    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
