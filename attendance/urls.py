from django.urls import path
from . import views

urlpatterns = [
    path('create-qr/', views.create_attendance_qr, name='create_qr'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('submit/', views.submit_attendance, name='submit_attendance'),
    path('attendance/<uuid:session_id>/', views.attendance_form, name='attendance_form'),
]
