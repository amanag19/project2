from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.inside , name='adminhome'),
    path('sellrreg' , views.sellrreg , name='sellerreg'),
    path('shopDetails/<shop_id>', views.shopDetails, name='shopDetails'),
    path('shopDetails/final/', views.final, name='final'),
]