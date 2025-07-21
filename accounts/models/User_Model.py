from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import RoleModel
from workers.models import WorkerModel

class UserModel(AbstractUser):
    role = models.CharField(choices=RoleModel, default='WORKER', max_length=15)
    linked_worker = models.OneToOneField(WorkerModel, on_delete = models.SET_NULL, null = True, blank = True, default=RoleModel.WORKER, related_name='user_account')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['role']

    def __str__(self):
        return f"{self.username} ({self.role})"