#From Python
from datetime import date

#From Django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
    ('male','Male'),
    ('female','Female'),
    ('other', 'Other')
)
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, default='male')
    mobile = models.BigIntegerField(default=0)
    address = models.TextField(null=True)
    details = models.TextField(null=True)
    medicine_detail = models.TextField(null=True)
    note = models.TextField(null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    next_visit = models.IntegerField(default=0)
    visit_date = models.DateField(default=timezone.now, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)  