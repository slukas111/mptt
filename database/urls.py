from django.urls import path
from database import views

urlpatterns = [
    path('', views.index, name='home')
]