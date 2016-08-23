from __future__ import unicode_literals
from django.db import models

class Appointment(models.Model):
    start_time = models.DateTimeField()
    start_date = models.DateField()
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey("loginreg.User", related_name = "creator")
