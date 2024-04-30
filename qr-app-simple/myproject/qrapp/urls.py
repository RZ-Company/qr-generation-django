from django.urls import path
from .views import generate_qr

urlpatterns = [
    path('qr/<path:data>/', generate_qr, name='generate_qr'),
]
