from django.db import models
from Auth_App.models import User
from django.db.models import Q
# Create your models here.


class TimeSession(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

class Attendance(models.Model):
    timeSession = models.ForeignKey(TimeSession, on_delete=models.CASCADE)
    attender = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    limit_choices_to=Q(is_teacher=True) | Q(is_superuser=True),
    related_name='attender'
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_student': True},
        related_name='student_attendances'
    )
    attendance = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)



    