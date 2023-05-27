from django.urls import include, re_path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'countries', views.CountryViewSet, basename="country")
router.register(r'cities', views.CitiesViewSet, basename="cities")

urlpatterns = [
    re_path(r'^', include(router.urls))
]
