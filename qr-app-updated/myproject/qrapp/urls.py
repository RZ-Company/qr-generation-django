from django.urls import path
from .views import generate_qr

urlpatterns = [
    path('qr/', generate_qr, name='generate_qr'),
]
