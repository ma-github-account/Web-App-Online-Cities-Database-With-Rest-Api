from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Country(models.Model):
    name = models.CharField(max_length=32)
    capitol = models.TextField(max_length=256)
    population = models.IntegerField()

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=32)
    population = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                             related_name='cities')

