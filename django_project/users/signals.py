from django.db.models.signals import post_save  # signal whenever an object is saved
from django.contrib.auth.models import User     # signal sender
from django.dispatch import receiver            # signal receiver (function that performs task after receiving the signal)
from .models import Profile


"""
Important note:
In order for signals to work properly:
    - they have to be imported to <app>/apps.py in the <app>Config class
    - the <app> import in <project>/settings.py has to be done with the whole <app>Config class name, not just '<app>'
"""

# A function triggering Profile creation whenever a User is being created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# A function triggering save Profile after a User has been saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


