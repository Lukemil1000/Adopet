from django.db import models
from django.contrib.auth.models import User, AbstractUser

USER_TYPE_CHOICES = (
    ('tutor', 'tutor'),
    ('shelter', 'shelter')
)

class Account(AbstractUser):
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

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
    
class Pet(models.Model):
    """Modelo para um pet"""

    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, null=False)
    name = models.CharField(null=False, max_length=50)
    description = models.TextField(blank=True)
    adopted = models.BooleanField(null=False, default=False)
    age = models.CharField(null=False, max_length=50)
    # picture = models.ImageField(null=True)
    # adoptions

    def __str__(self) -> str:
        return self.name
    
class Adoption(models.Model):
    "Modelo para adoção"

    pet = models.OneToOneField(Pet, on_delete=models.CASCADE, null=False)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=False)
    date = models.DateField(null=False)