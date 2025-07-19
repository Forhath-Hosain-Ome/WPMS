from django.db import models
from core.models import GenderModel, DepertmentModel, DesignationModel, EmploymentTypeModel
from phonenumber_field.modelfields import PhoneNumberField

class WorkerModel(models.Model):
    worker_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    gender = models.CharField(choices=GenderModel,max_length=10, default='')
    date_of_birth = models.DateField()
    contact_number = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=60)
    join_date = models.DateField(auto_now_add=True)
    depertment = models.CharField(choices=DepertmentModel, default='', max_length=10)
    designaton = models.CharField(choices=DesignationModel, default='', max_length=10)
    employment_type = models.CharField(choices=EmploymentTypeModel, max_length=10, default='')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
        ordering = ['depertment', 'designaton', 'employment_type', 'status']