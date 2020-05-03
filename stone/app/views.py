from json import JSONEncoder

from django.contrib.messages import api
from rest_framework import viewsets
from datetime import datetime

from itertools import chain

from stone.app.filters import CustomSearchFilter, StartypeFilter
from stone.app.serializers import *
from stone.models import *
from django.db.models import Q
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

zodiacs = [(1900, "1"), (1901, "2"), (1902, "3"), (1903, "4"), (1904, "5"),
          (1905, "6"), (1906, "7"), (1907, "8"), (1908, "9"),
          (1909, "10"), (1910, "11"), (1911, "12")]


def getChineseZodiac(year):
    index = (year - zodiacs[0][0]) % 12
    return zodiacs[index]


def digSum(n):
    if n == 0:
        return 0
    if n % 9 == 0:
        return 9
    else:
        return n % 9

class StoneViewset(viewsets.ModelViewSet):
    # queryset = stone.objects.all()
    serializer_class = StoneSerializer

    # filter_backends = (DjangoFilterBackend, CustomSearchFilter,)
    # filterset_fields = {'star','day_of_week','number' }
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ['stone_name_th', 'stone_name_en', 'description', 'color', ]

    def get_queryset(self):
        my_filter = Q()
        argumentos = {}
        w = []
        search = ""
        search_filter = Q()
        attribute_filter = Q()
        count = 0
        queryset = Startype.objects.all()
        date_str = self.request.query_params.get('date',None)
        query_date = None
        if date_str is not None:
            query_date = datetime.strptime(date_str, '%d-%m-%Y')
            d_str = date_str.split('-')
            print(datetime.strptime(date_str, '%d-%m-%Y')),
            my_filter |= Q(**{'number': digSum(int(''.join(d_str)))})
            my_filter |= Q(**{'day_of_mouth__contains': '{' + str(query_date.day) + '}'})
            my_filter |= Q(**{'month_of_year__contains': '{' + str(query_date.month) + '}'})
            if self.request.query_params.get('isNight'):
                my_filter |= Q(**{'day_of_week': 7})
            else:
                my_filter |= Q(**{'day_of_week': query_date.weekday()})
            # search_filter |= Q(**{'zodiac': getChineseZodiac(query_date.year)})
            # print(str(datetime. strptime(date_str, '%d-%m-%Y').day))
        # if self.request.query_params.get('day_of_week'):
        #     # argumentos['day_of_week'] = self.request.query_params.get('day_of_week')
        #     count += 1
        #     my_filter |= Q(**{'day_of_week': self.request.query_params.get('day_of_week')})

        # if self.request.query_params.get('number'):
        #     # argumentos['number'] = self.request.query_params.get('number')
        #     count += 1
        #     my_filter |= Q(**{'number': self.request.query_params.get('number')})

        # if self.request.query_params.get('day_of_mouth'):
        #     # argumentos['day_of_mouth'] = self.request.query_params.get('day_of_mouth')
        #     count += 1
        #     my_filter |= Q(**{'day_of_mouth__contains': '{' + self.request.query_params.get('day_of_mouth') + '}'})

        # if self.request.query_params.get('month_of_year'):
        #     # argumentos['month_of_year'] = self.request.query_params.get('month_of_year')
        #     count += 1
        #     my_filter |= Q(**{'month_of_year__contains': '{' + self.request.query_params.get('month_of_year') + '}'})

        if self.request.query_params.get('search'):
            # argumentos['search'] = self.request.query_params.get('search')
            search = self.request.query_params.get('search')
            search_filter |= Q(**{'color__contains': search})
            search_filter |= Q(**{'stone_name_th__contains': search})
            search_filter |= Q(**{'stone_name_en__contains': search})
            search_filter |= Q(**{'description__contains': search})

        if self.request.query_params.get('attribute'):
            attribute = self.request.query_params.get('attribute')
            attribute = attribute.split(',')
            print(attribute)
            for a in attribute:
                search_filter |= Q(**{'attribute__in':  a})

        if date_str is None:

            return stone.objects.filter(search_filter)

        mystone_filter = Q()
        for s in Startype.objects.filter(my_filter):
            mystone_filter |= Q(**{'star': s})
        print(mystone_filter)
        print(stone.objects.filter(mystone_filter))
        return stone.objects.filter((mystone_filter | Q(**{'zodiac': getChineseZodiac(query_date.year)})) & search_filter )


# class StoneCreateModelViewSet(viewsets.ModelViewSet):
#     serializer_class = StoneCreateSerializer
#     queryset = Attributes.objects.all()


class AttributeModelViewSet(viewsets.ModelViewSet):
    serializer_class = AttributeSerializer
    queryset = Attribute.objects.all()


# class AttributeViewset (viewsets.ModelViewSet):
#     queryset = attribute.objects.all()
#     serializer_class = AttributeSerializer


# class StoneViewset


# class StoneStoneViewset(generics.ListCreateAPIVie, viewsets.ModelViewSet):
#     queryset = stone.objects.all()
#     serializer_class = StoneSerializer
#
#
# class StoneDetail(generics.RetrieveUpdateDestroyAPIView, viewsets.ModelViewSet):
#     queryset = stone.objects.all()
#     lookup_field = 'id'
#     serializer_class = StoneSerializer

class FaveriteModelViewSet(viewsets.ModelViewSet):
    serializer_class = FaveriteCreateSerializer
    queryset = Favorite.objects.all()
    filterset_fields = ['user', ]


class FaveriteFBModelViewSet(viewsets.ModelViewSet):
    serializer_class = FaveriteFBCreateSerializer
    queryset = Favorite_FB.objects.all()
    filterset_fields = ['user', 'Stone']


class stoneIMGModelViewSet(viewsets.ModelViewSet):
    serializer_class = stoneIMGSerializer
    queryset = StoneIMG.objects.all()


class ZodiacModelViewSet(viewsets.ModelViewSet):
    serializer_class = ZodiacSerializer
    queryset = Zodiac.objects.all()


class BraceletPatternModelViewSet(viewsets.ModelViewSet):
    serializer_class = BraceletPatternSerializer
    queryset = BraceletPattern.objects.all()
    filterset_fields = ['user_id']





class StartypeViewSet(viewsets.ModelViewSet):
    serializer_class = StartypeSerializer

    # queryset = None
    # filterset_fields = ['day_of_week','number','day_of_mouth','month_of_year']
    # filterset_class = { StartypeFilter,}

    def get_queryset(self):
        my_filter = Q()
        argumentos = {}
        w = []
        queryset = Startype.objects.all()
        if self.request.query_params.get('day_of_week'):
            argumentos['day_of_week'] = self.request.query_params.get('day_of_week')
            my_filter |= Q(**{'day_of_week': argumentos['day_of_week']})

        if self.request.query_params.get('number'):
            argumentos['number'] = self.request.query_params.get('number')
            my_filter |= Q(**{'number': argumentos['number']})

        if self.request.query_params.get('day_of_mouth'):
            argumentos['day_of_mouth'] = self.request.query_params.get('day_of_mouth')
            my_filter |= Q(**{'day_of_mouth__contains': '{' + argumentos['day_of_mouth'] + '}'})

        if self.request.query_params.get('month_of_year'):
            argumentos['month_of_year'] = self.request.query_params.get('month_of_year')
            my_filter |= Q(**{'month_of_year__contains': '{' + argumentos['month_of_year'] + '}'})
        print(my_filter)
        if len(argumentos) <= 0:
            return Startype.objects.all()
        print(Startype.objects.filter(my_filter))
        return Startype.objects.filter(my_filter)
