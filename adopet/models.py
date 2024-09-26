from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    """Modelo de usuário para um tutor"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=11)
    city = models.CharField(blank=True, max_length=50)
    about = models.TextField(blank=True)
    # picture = models.ImageField(null=True)
    # adoptions

    def __str__(self) -> str:
        return self.user.username
    
class Shelter(models.Model):
    """Modelo de usuário para um abrigo"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cnpj = models.CharField(null=False, unique=True, max_length=14)
    name = models.CharField(null=False, max_length=50)
    phone = models.CharField(null=False, max_length=11)
    adress = models.CharField(null=False, max_length=50)
    about = models.TextField(blank=True)
    # picture = models.ImageField(null=True)
    # pets
    # adoptions

    def __str__(self) -> str:
        return self.user.username