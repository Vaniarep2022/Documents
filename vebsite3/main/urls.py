from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('reshka/', views.reshka),
    path('about/', views.about),
]
