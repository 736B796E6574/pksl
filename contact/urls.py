from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    # ... any other URL patterns for the home app ...
]
