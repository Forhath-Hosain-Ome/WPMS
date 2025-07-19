from django.db import models
from accounts.models import UserModel
from core.models import LeaveTypeModel, StatusModel

class LeaveModel(models.Model):
    worker = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='worker')
    leave_type = models.CharField(choices=LeaveTypeModel, default='')
    start_date = models.TimeField()
    end_date = models.TimeField()
    status = models.CharField(choices=StatusModel, default='')
    approved_by = models.OneToOneField(UserModel, limit_choices_to={'role__in': ['ADMIN', 'HR', 'SUPERVISOR']}, on_delete=models.CASCADE)