from django.db import models

class GenderModel(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHERS = 'Others'