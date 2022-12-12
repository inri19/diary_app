from django.urls import path
from .views import *

urlpatterns = [
    path('inscription/', inscription, name='inscription'),
] 