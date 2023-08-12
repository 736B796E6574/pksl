from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ... any other URL patterns for the home app ...
]
