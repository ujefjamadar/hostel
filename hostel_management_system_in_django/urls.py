from django.contrib import admin
from django.urls import path, include  # Import include here
# Import views from guest app if necessary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guest.urls')),  # Include guest app's URLs
]
