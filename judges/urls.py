from django.contrib import admin
from django.urls import path, include

app_name = 'judges'
urlpatterns = [
    path('<int:problem_id>/', views.judge, name='judge'),
]
