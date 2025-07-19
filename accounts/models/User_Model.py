from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import RoleModel
from workers.models import WorkerModel

class UserModel(AbstractUser):
    role = models.CharField(choices=RoleModel, default='WORKER')
    linked_worker = models.OneToOneField(WorkerModel, on_delete = models.CASCADE, null = True, blank = True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['role']