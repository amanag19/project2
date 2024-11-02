from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.loginUser , name="login_form"),
    path('logout' , views.logout , name='logout'),
]