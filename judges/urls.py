from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'judges'
urlpatterns = [
    path('<int:problem_id>/', views.judge, name='judge'),
    path('<int:problem_id>/result', views.judge, name='result')
]
