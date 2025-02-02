from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path('insert-sensor/', views.insert_sensor, name='insert_sensor'),
    path('insert-user/', views.insert_user, name='insert_user'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]