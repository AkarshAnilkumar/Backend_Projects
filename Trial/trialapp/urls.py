from django.urls import path
# from .import views
from .views import pie_chart, hi


urlpatterns = [
    # path('employees/', views.employees, name='employees'),
    # path('', views.index, name='index'),
    path('a/', hi, name='base'),
    # path('forms/', forms, name='forms'),
    path('pie-chart/', pie_chart, name='pie-chart'),
]
