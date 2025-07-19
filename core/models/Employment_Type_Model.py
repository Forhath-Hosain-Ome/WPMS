from django.db import models

class EmploymentTypeModel(models.TextChoices):
    FULL_TIME = 'Full-Time'
    PART_TIME = 'Part-Time'
    CONTRACT = 'Contracts'