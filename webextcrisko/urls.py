from django.urls import path
from .views import parse_html
from .views import extension_login

urlpatterns = [
    path('parse_html/', parse_html, name='parse_html'),
    path('extension_login/', extension_login, name='extension_login')
]
