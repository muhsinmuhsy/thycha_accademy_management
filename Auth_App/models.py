from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER,  null=True, blank=True)
    image = models.ImageField(upload_to='teacher-images' ,null=True, blank=True)