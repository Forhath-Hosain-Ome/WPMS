from django.db import models
from workers.models import WorkerModel
from .Shift_Model import Shift

class WorkShift(models.Model):
    worker = models.ForeignKey(WorkerModel, on_delete=models.CASCADE)
    shift = models.OneToOneField(Shift, on_delete=models.CASCADE)
    assignment_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)