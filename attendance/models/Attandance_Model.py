from django.db import models
from workers.models import WorkerModel
from attendance.models import ShiftModel
from core.models import AttandanceStatus

class AttandanceModel(models.Model):
    worker = models.OneToOneField(WorkerModel, on_delete=models.CASCADE)
    shift = models.OneToOneField(ShiftModel, on_delete=models.CASCADE)
    date = models.DateField(auto_created=True)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    status = models.CharField(choices=AttandanceStatus, max_length=10)
    worked_hour = models.IntegerField()