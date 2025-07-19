from django.db import models

class RoleModel(models.TextChoices):
    ADMIN = 'Admin'
    HR = 'Hr'
    SUPERVISOR = 'Supervisor'
    WORKER = 'Worker'