from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.registerUser, name='register_form'),
]