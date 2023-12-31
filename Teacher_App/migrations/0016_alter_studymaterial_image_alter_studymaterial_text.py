# Generated by Django 4.2.3 on 2023-11-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher_App', '0015_studymaterial_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studymaterial',
            name='image',
            field=models.ImageField(null=True, upload_to='study-material'),
        ),
        migrations.AlterField(
            model_name='studymaterial',
            name='text',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
