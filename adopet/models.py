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