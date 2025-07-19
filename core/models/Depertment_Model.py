from django.db import models

class DepertmentModel(models.TextChoices):
    SEWING = 'Sewing'
    FINISHING = 'Finishing'
    WASH = 'Wash'
    SECURITY = 'Security'