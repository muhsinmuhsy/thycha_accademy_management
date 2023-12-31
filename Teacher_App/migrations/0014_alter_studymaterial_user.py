# Generated by Django 4.2.3 on 2023-11-01 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Teacher_App', '0013_studymaterial_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studymaterial',
            name='user',
            field=models.ForeignKey(limit_choices_to=models.Q(('is_teacher', True), ('is_superuser', True), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, related_name='studymaterial_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
