from django.urls import path, include
from . import views

urlpatterns = [
    path('course/', views.index, name='index'),
]