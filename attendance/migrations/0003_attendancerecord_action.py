# Generated by Django 5.1.7 on 2025-04-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_faculty_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancerecord',
            name='action',
            field=models.CharField(choices=[('login', 'Login'), ('logout', 'Logout')], default='login', max_length=10),
            preserve_default=False,
        ),
    ]
