from django.dispatch import receiver
from django.db.models.signals import post_delete
from adopet.models import Tutor, Shelter

@receiver(post_delete, sender=Tutor)
@receiver(post_delete, sender=Shelter)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user: 
        instance.user.delete()