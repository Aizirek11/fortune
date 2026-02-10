from django.urls import path
from .views import index, options_api, spin_api, delete_all_options

urlpatterns = [
    path('', index),
    path('api/options/', options_api),
    path('api/options/clear/', delete_all_options),
    path('api/spin/', spin_api),
]
