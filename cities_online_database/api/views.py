from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions
)
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action

from api.serializers import UserSerializer
from .models import Country, City
from .serializers import CountrySerializer, CitySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('name', 'capitol', 'population')
    search_fields = ('name', 'capitol')
    ordering_fields = '__all__'
    ordering = ('name',)

    def get_queryset(self):
        countries = Country.objects.all()
        return countries

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CountrySerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        country = Country.objects.create(name=request.data['name'],
                               capitol=request.data['capitol'],
                               population=request.data['population'])
        serializer = CountrySerializer(country, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        country = self.get_object()
        country.name = request.data['name']
        country.capitol = request.data['capitol']
        country.population = request.data['population']
        country.save()

        serializer = CountrySerializer(country, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        country = self.get_object()
        country.delete()
        return Response('Country deleted')

class CitiesViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer












