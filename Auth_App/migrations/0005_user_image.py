# Generated by Django 4.2.3 on 2023-09-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_App', '0004_remove_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]