from django.db import models
import uuid

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pin = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class AttendanceSession(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Session {self.session_id}"

class AttendanceRecord(models.Model):
    session = models.ForeignKey(AttendanceSession, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=10, choices=[('login', 'Login'), ('logout', 'Logout')])

    def __str__(self):
        return f"{self.faculty.name} - {self.action} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
