from django.dispatch import receiver
from django.db.models.signals import post_delete, post_init
from adopet.models import Tutor, Shelter, Adoption

@receiver(post_delete, sender=Tutor)
@receiver(post_delete, sender=Shelter)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user: 
        instance.user.delete()

@receiver(post_init, sender=Adoption)
def post_init_change_pet_adopted(sender, instance, *args, **kwargs):
    if instance.pet:
        instance.pet.adopted = True
        instance.pet.save()

@receiver(post_delete, sender=Adoption)
def post_delete_change_pet_adopted(sender, instance, *args, **kwargs):
    if instance.pet:
        instance.pet.adopted = False
        instance.pet.save()