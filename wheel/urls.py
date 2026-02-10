from django.urls import path
from .views import index, options_api, spin_api

urlpatterns = [
    path('', index),
    path('api/options/', options_api),
    path('api/spin/', spin_api),
]

