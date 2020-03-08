from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', '')

    ]
    user =  models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    dob  = models.DateField(auto_now=False, auto_now_add=False,default=date.today)

    class Meta:
        ordering = ['user']
