from django.db import models
from workers.models import WorkerModel
from core.models import StatusModel

class PayrollModel(models.Model):
    worker = models.OneToOneField(WorkerModel, on_delete=models.CASCADE)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    base_salary = models.IntegerField()
    overtime_hour = models.IntegerField()
    overtime_pay = models.IntegerField()
    deductions = models.IntegerField()
    net_sallary = models.IntegerField()
    generated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=StatusModel, max_length=15)