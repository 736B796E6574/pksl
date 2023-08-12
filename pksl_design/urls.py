from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),  # Including the home app's URLs here
    # ... any other URL patterns ...
]
