from rest_framework import serializers
from rest_framework.utils import json

from stone.models import *


# from drf_extra_fields.fields import Base64ImageField


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format

            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                data = data.replace('.', '=')
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'attribute_name')

    # def create(self, validated_data):
    #     return attribute.objects.create(**validated_data)


class StoneSerializer(serializers.ModelSerializer):
    # attribute = serializers.ListField(child=serializers.IntegerField(), allow_empty=True, required=False)
    # notusewith = serializers.ListField(child=serializers.IntegerField(), allow_empty=True, required=False)
    stone_img = Base64ImageField(
        max_length=None, use_url=True, required=False
    )
    stone_img_sm = Base64ImageField(
        max_length=None, use_url=True, required=False
    )

    class Meta:
        model = stone
        # fields = ('id', 'stone_name_th', 'stone_name_en', 'color', 'description', 'stone_img', 'attribute',
        #           'src_img', 'stone_img_sm','chemical_formula','star',)
        fields = '__all__'
        ordering = ('stone_name_en', 'id')

    # def to_internal_values(self, data):
    #     if isinstance(data['attribute'], str):
    #         data['attribute'] = json.loads(data['attribute'])
    #     if isinstance(data['notusewith'], str):
    #         data['notusewith'] = json.loads(data['notusewith'])
    #     print(data)
    #     return data
    # civilians = serializers.IntegerField(default=0, required=False)

    # def create(self, validated_data):
    #     print(validated_data)
    #     return validated_data
    def create_or_update(self, validated_data):
        attributes = validated_data.pop('attribute')
        print(attributes)
        stone_data = stone.objects.create(**validated_data)
        if len(attributes) > 0:
            for a in attributes:
                stone_data.attribute.add(a)
        return stone_data


    # def patch(self, instance, validated_data):
    #     print(instance)
    #     print(validated_data)
    #     stone_data = stone.objects.filter(pk=instance.id)
    #     print(stone_data)
    #     attributes = []
    #     if validated_data.get('attribute'):
    #         attributes = validated_data.pop('attribute')
    #     if validated_data:
    #         stone_data.update(**validated_data)
    #     new_data = stone.objects.get(pk=instance.id)
    #     if len(attributes) > 0:
    #         print(new_data.attribute.values())
    #         for a in new_data.attribute.values():
    #             new_data.attribute.remove(a.get('id'))
    #         for a in attributes:
    #             new_data.attribute.add(a)
    #     return new_data


# class StoneWithAttributeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attributes
#         fields = ('stone',)


# class StoneCreateSerializer(serializers.ModelSerializer):
#     # Attributes = StoneWithAttributeSerializer(many=True)
#
#     def create(self, validated_data):
#         attributes_data = validated_data.pop('attribute')
#         stones = stone.objects.create(**validated_data)
#         for attributes in attributes_data:
#             d = dict(attributes)
#             Attributes.objects.create(stone=stones, attribute=d['attributes'])
#         return stone
#
#     class Meta:
#         model = stone
#         fields = '__all__'

class FaveriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    # def create(self, validated_data,**kwargs):
    #     print(kwargs)
    #     user_data = validated_data.pop('user')
    #     stone_data = validated_data.pop('Stone')
    #     print(user_data)
    #     print(stone_data)
    #     fav = Favorite.objects.create(user=user_data,stone=stone_data)
    #     return fav


class FaveriteFBCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite_FB
        fields = '__all__'


class stoneIMGSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoneIMG
        fields = '__all__'


class stoneIMGSMSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoneIMGSM
        fields = '__all__'


class StartypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startype
        fields = ('id', 'name',
                  'day_of_week',
                  'day_of_mouth',
                  'month_of_year',
                  'number')


class ZodiacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zodiac
        fields = '__all__'


class BraceletPatternSerializer(serializers.ModelSerializer):
    NumOfStones = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    wristSize = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    stoneSize = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = BraceletPattern
        fields = '__all__'