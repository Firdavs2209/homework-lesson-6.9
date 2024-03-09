from django.urls import path
from .views import theme_list

urlpatterns = [
    path('', theme_list, name='theme_list'),
]
