from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatars/',default='avatar/defaults.png',blank=True)
    bio=models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    

@receiver(post_save,sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        from .models import Profile
        Profile.objects.create(user=instance)



@receiver(post_save,sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
        
