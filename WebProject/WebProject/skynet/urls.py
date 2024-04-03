from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('services', services, name="services"),
    path('', index, name="clients"),
    path('', index, name="login"),
    path("service/<int:id>", service, name="service")
    
]
