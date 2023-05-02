from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('home/', views.home),
    path('room/1', views.room),
    path('room/2', views.room2),
    path('room/3', views.room3),
]
