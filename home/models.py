from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name= "Покупатель", related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    location = models.CharField(max_length=50, blank=True, verbose_name="Местожительство")
    objects = models.Manager()

    def get_absolute_url(self):
        return f'/account/'    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()