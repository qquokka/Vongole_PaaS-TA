from django.urls import path
from . import views

app_name = "problems"

urlpatterns = [
    path('', views.index, name="index"),
    path('subject/', views.subject, name="subject"),
    path('subject/category/', views.category, name="category"),
]