import django_filters
from django_filters import rest_framework, CharFilter
from rest_framework import filters
from django.contrib.postgres.fields import  ArrayField

from stone.models import Startype


class CustomSearchFilter(filters.SearchFilter):
    """"Dynamically change search fields based on request content."""

    def get_search_fields(self, view, request):
        """
        Search only on the title or the article body if the query parameter,
        title_only or article_only is in the request.
        """
        # request.query_params is a more correctly named synonym for request.GET
        # request.GET a dictionary-like object containing
        # all given HTTP GET parameters

        # Get the value of the "title_only" item
        # How does the querydict looks like
        # <QueryDict: {'search': ['Sometitle'], 'title_only': ['title_only']}>

        # if exist return search_fields with ['title'] only
        if request.query_params.get('star'):
            return ['star']
        elif request.query_params.get('number'):
            return ['number']
        return super(CustomSearchFilter, self).get_search_fields(view, request)


class StartypeFilter(rest_framework.FilterSet):
    day_of_mouth = CharFilter(lookup_expr='icontains')
    month_of_year = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Startype
        fields = ('day_of_week','number')
        filter_overrides = {
             ArrayField: {
                 'filter_class': django_filters.CharFilter,
             }
        }

