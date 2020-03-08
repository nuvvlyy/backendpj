import hashlib
import hmac
import base64
from django.core.serializers import json
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from auth.app.serializers import UserSerializer,UserProfileSerializer,  FaceBookUserProfileSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
import crypt
from django.conf import settings


# class UserView(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
from stone.models import UserProfile, FaceBookUserProfile


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # filterset_fields = ['email','password']

    # @property
    # def get_queryset(self,):
    #     # email = self.request.GET['email']
    #     if 'username'in self.request.GET:
    #         _username = self.request.GET['username']
    #         _password = self.request.GET['password']
    #         print(_password)
    #         print(_username)
    #         user = User.objects.filter(username=_username).values()[0]
    #         # d = dict(user)
    #         print(user['password'])
    #         first_pass = user['password'].split('$')
    #         print(first_pass)
    #         hasher = first_pass[0]
    #         salt = first_pass[1]  # grabbing salt from the first password of the database
    #         pws = make_password('password1234',salt,hasher)
    #         print(pws)
    #         # user = authenticate(username=username, password='_password')
    #
    #         if user is not None:
    #             print('fufu1234')
    #         return User.objects.all()
    #     else:
    #         print('fufufufuf')
    #     return User.objects.all()
    # def get_queryset(self,*args,**kwargs):
    #     """
    #
    #     :param query:
    #     :type kwarg: object
    #     """

    #
    #


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filterset_fields = ['user']


class FaceBookUserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = FaceBookUserProfileSerializer
    queryset = FaceBookUserProfile.objects.all()
    filterset_fields = ['email']