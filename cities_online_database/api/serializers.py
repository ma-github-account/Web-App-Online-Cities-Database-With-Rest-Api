from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Country, City
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.population = validated_data.get('population', instance.population)
        instance.save()

        return instance

class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)

    class Meta:
        model = Country
        fields = ('id','name', 'capitol', 'population','cities')
        read_only_fields = ('cities',)

class CountryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')



