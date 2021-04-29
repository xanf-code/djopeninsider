from django.urls import path, include
from .views import index, insiderAPI, latest
from rest_framework import routers

router = routers.DefaultRouter()
router.register("getRecentData", insiderAPI)

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('fetchlatestdata', latest, name='latest'),
]
