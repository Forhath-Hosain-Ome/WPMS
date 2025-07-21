from django.db import models
from accounts.models import UserModel
from core.models import LeaveTypeModel, StatusModel

class LeaveModel(models.Model):
    worker = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='worker')
    leave_type = models.CharField(choices=LeaveTypeModel, default='')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=StatusModel, default='')
    approved_by = models.ForeignKey(
        UserModel, 
    limit_choices_to={'role__in': ['ADMIN', 'HR', 'SUPERVISOR']},
    on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.worker.username} - {self.leave_type} ({self.start_date} to {self.end_date})"