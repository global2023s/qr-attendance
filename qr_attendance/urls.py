# qr_attendance/urls.py

from django.contrib import admin
from django.urls import path, include  # include is required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('attendance.urls')),  # ✅ This tells Django: look in attendance/urls.py for anything starting with /api/
]
