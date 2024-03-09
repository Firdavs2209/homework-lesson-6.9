from django.urls import path

from app_pupils.views import talaba,talaba1

urlpatterns = [
    path('<int:pk>', talaba1, name='talaba1', ),
    path('', talaba, name='talaba'),
]
