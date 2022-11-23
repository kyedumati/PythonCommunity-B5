from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('welcome/', views.welcome_view),
    path('add_employee/', views.add_employee),
]