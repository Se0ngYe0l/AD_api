from django.urls import path

from . import views

app_name='adAPI'
urlpatterns = [
    path('ad/', views.class_func),
]