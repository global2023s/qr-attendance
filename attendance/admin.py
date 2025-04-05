from django.contrib import admin
from .models import Faculty, AttendanceSession, AttendanceRecord

# Register your models here
admin.site.register(Faculty)
admin.site.register(AttendanceSession)
admin.site.register(AttendanceRecord)
