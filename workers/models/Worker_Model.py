from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from core.models import GenderModel, DepertmentModel, DesignationModel, EmploymentTypeModel, WorkerStatus


class WorkerModel(models.Model):
    worker_id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(choices=GenderModel.choices,max_length=10, default='MALE')
    date_of_birth = models.DateField()
    contact_number = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    join_date = models.DateField(auto_now_add=True)
    department = models.CharField(choices=DepertmentModel.choices, max_length=10, default='')
    designation = models.CharField(choices=DesignationModel.choices, max_length=10, default='')
    employment_type = models.CharField(choices=EmploymentTypeModel.choices, max_length=10, default='')
    status = models.CharField(choices=WorkerStatus.choices, max_length=15)

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
        ordering = ['department', 'designation', 'employment_type', 'status']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.worker_id})"