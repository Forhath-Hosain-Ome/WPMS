from django.db import models
from workers.models import WorkerModel
from core.models import StatusModel
from attendance.models import Attendance

class PayrollModel(models.Model):
    worker = models.ForeignKey(WorkerModel, on_delete=models.SET_NULL, null=True)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    base_salary = models.DecimalField(max_digits=6, decimal_places=2)
    overtime_hour = models.DurationField()
    overtime_pay = models.DecimalField(max_digits=6, decimal_places=2)
    deductions = models.DecimalField(max_digits=6, decimal_places=2)
    net_sallary = models.DecimalField(max_digits=6, decimal_places=2)
    generated_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=StatusModel.choices, max_length=15)

    class Meta:
        verbose_name = 'Payroll'
        verbose_name_plural = 'Payrolls'
        ordering = ['-generated_date']

    def __str__(self):
        return f"Payroll for {self.worker} ({self.pay_period_start} to {self.pay_period_end})"
    
    @property
    def total_overtime(self):
        pass