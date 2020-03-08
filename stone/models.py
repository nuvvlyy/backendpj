from datetime import date

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User



# Create your models here.
class Attribute(models.Model):
    attribute_name = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '%d: %s' % (self.id, self.attribute_name)


class Startype(models.Model):
    name =models.CharField(max_length=150, blank=True, null=True)
    day_of_week = models.CharField(max_length=150)
    day_of_mouth = ArrayField(models.IntegerField(), default=list)
    month_of_year = ArrayField(models.IntegerField(), default=list)
    number = models.IntegerField()

    # def __str__(self):
    #     return '%d: %s' % (self.id, self.name)
    def __str__(self):
        return self.name

class stone(models.Model):
    id = models.AutoField(primary_key=True)
    stone_name_th = models.CharField(max_length=150)
    stone_name_en = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    attribute = models.ManyToManyField(Attribute, related_name='attribute', null=True, blank=True)
    stone_img = models.ImageField(upload_to="stone", blank=True, null=True)
    src_img =models.CharField(max_length=150, blank=True, null=True)
    stone_img_sm = models.ImageField(upload_to="stone_sm", blank=True, null=True)
    chemical_formula =models.CharField(max_length=200, blank=True, null=True)
    star = models.ForeignKey(Startype, on_delete=models.CASCADE,  blank=True, null=True)
    element = models.CharField(max_length=150,  blank=True, null=True)
    ancient_name = models.CharField(max_length=150,  blank=True, null=True)
    day_of_week = models.IntegerField( blank=True, null=True)
    number = models.IntegerField( blank=True, null=True)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return '%d: %s' % (self.id, self.stone_name_en)

    class Meta:
        ordering = ['stone_name_en']




class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Stone = models.OneToOneField(stone, on_delete=models.CASCADE, related_name='stone')


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', '')

    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False, auto_now_add=False,default=date.today)


    class Meta:
        ordering = ['user']


class FaceBookUserProfile(models.Model):
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)
    email = models.EmailField('email address', blank=True, unique=True )
    dob = models.DateField(auto_now=False, auto_now_add=False,default=date.today)

    class Meta:
        ordering = ['pk']


class Favorite_FB(models.Model):
    user = models.ForeignKey(FaceBookUserProfile, on_delete=models.CASCADE)
    Stone = models.ForeignKey(stone, on_delete=models.CASCADE)


class user(models.Model):
    # password = models.c
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)
    email = models.EmailField('email address', blank=True, unique=True )
    dob = models.DateField(auto_now=False, auto_now_add=False,default=date.today)


class StoneIMG(models.Model):
    img = models.FileField(upload_to="stone", blank=True, null=True)


class StoneIMGSM(models.Model):
    img = models.FileField(upload_to="stone_sm", blank=True, null=True)



