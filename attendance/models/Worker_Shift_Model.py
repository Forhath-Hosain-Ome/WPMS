from django.db import models
from workers.models import WorkerModel
from .Shift_Model import ShiftModel

class WorkShift(models.Model):
    worker = models.ForeignKey(WorkerModel, on_delete=models.CASCADE)
    shift = models.ForeignKey(ShiftModel, on_delete=models.CASCADE)
    assignment_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Work Shift"
        verbose_name_plural = "Work Shifts"
        ordering = ['-assignment_date']

    def __str__(self):
        return f"{self.worker.first_name} {self.worker.last_name} - {self.shift.shift_name}"