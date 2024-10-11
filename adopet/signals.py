from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from adopet.models import Tutor, Shelter, Adoption

@receiver(post_delete, sender=Tutor)
@receiver(post_delete, sender=Shelter)
def post_delete_account(sender, instance, *args, **kwargs):
    if instance.account: 
        instance.account.delete()

@receiver(post_save, sender=Adoption)
def post_init_change_pet_adopted(sender, instance, created, *args, **kwargs):
    if created and instance.pet:
        instance.pet.adopted = True
        instance.pet.save()

@receiver(post_delete, sender=Adoption)
def post_delete_change_pet_adopted(sender, instance, *args, **kwargs):
    if instance.pet:
        instance.pet.adopted = False
        instance.pet.save()