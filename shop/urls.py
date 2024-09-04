from django.urls import path
from shop.views import *

urlpatterns = [
    path('drink/', drink),
    path('about/',about),
    path('content/',content),
    path('create/', create),
    path('detail/<str:p_id>/', detail),
    path('delete/<str:p_id>', delete),
    path('order/<str:p_id>', order)
] 