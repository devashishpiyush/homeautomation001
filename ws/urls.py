from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getEsp/<str:espId>/', views.getEsp, name='getEsp'),
    path('setEsp/<int:itemId>/<int:value>/', views.setEsp, name='setEsp'),
]