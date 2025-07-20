from django.db import models

class ShiftModel(models.Model):
    shift_name = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    break_duration = models.CharField()
    overtime_rate = models.DecimalField()