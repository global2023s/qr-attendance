from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('attendance.urls')),  # for API endpoints
    path('', include('attendance.urls')),      # this allows faculty-login/ to work
]
