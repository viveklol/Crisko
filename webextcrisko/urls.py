from django.urls import path
from .views import parse_html

urlpatterns = [
    path('parse_html/', parse_html, name='parse_html')
]
