# Generated by Django 4.2.3 on 2023-10-14 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher_App', '0002_alter_attendance_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='user',
            new_name='attender',
        ),
    ]
