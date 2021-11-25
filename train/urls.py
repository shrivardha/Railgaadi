from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='train-home'),
    path('about/', views.about,name='train-about'),
    
]