from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.settings import api_settings

from stone.models import UserProfile, FaceBookUserProfile
from backend.CustomException import CustomExcpetion


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def create(self, validated_data, username=None, password=None):
        users = User.objects.create(**validated_data)
        users.set_password(validated_data['password'])
        users.save()
        return users


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'


    def create(self , validated_data):
        d = validated_data.pop('dob')
        user_data = validated_data['user']['password']
        users = User.objects.create(**validated_data['user'])
        var = {'password': user_data}
        users.set_password(var)
        users.save()
        User_Profile = UserProfile.objects.create(user=users, dob=d)
        return User_Profile



# class USERSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'username', 'password','DOB')
#         related_fields = ['user_profile']
#
#     DOB = serializers.DateField(source='user_profile.dob')  # this is your related_name
#
#     def update(self, instance, validated_data):
#         # Handle related objects
#         for related_obj_name in self.Meta.related_fields:
#
#             # Validated data will show the nested structure
#             data = validated_data.pop(related_obj_name)
#             related_instance = getattr(instance, related_obj_name)
#
#             # Same as default update implementation
#             for attr_name, value in data.items():
#                 setattr(related_instance, attr_name, value)
#             related_instance.save()
#         return super(ABSerializer, self).update(instance, validated_data)

class  FaceBookUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaceBookUserProfile
        fields = '__all__'