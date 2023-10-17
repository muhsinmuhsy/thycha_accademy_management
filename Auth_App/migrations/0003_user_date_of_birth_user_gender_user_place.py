# Generated by Django 4.2.3 on 2023-09-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_App', '0002_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
