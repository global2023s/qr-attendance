from django.urls import path
from . import views

urlpatterns = [
    path('faculty-login/<uuid:session_id>/', views.attendance_form, name='attendance_form'),
]
