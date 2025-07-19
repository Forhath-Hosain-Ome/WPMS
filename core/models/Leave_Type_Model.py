from django.db import models

class LeaveTypeModel(models.TextChoices):
    SICK = 'Sick'
    CASUAL = 'Casual'
    EARNED = 'Earned'