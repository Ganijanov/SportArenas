from django.urls import path
from main import views

urlpatterns = [
    path('', views.mp, name='mp_url'),
    path('detail/<int:id>/', views.detail, name='detail_url'),
    path('arenalar/', views.arenalar, name='arenalar_url'),
    path('sport/', views.sport, name='sport_url'),
    path('viloyat/<int:id>/', views.viloyatlar, name='viloyat_url'),
    path('sport/<int:id>/', views.sportdet, name='sportdet_url'),
]       