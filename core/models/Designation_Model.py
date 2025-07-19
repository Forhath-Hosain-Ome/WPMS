from django.db import models

class DesignationModel(models.TextChoices):
    OFFICER = 'Officer'
    INCHARGE = 'Incharge'
    MANAGER = 'Manager'