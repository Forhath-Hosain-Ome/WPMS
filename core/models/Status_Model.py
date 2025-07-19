from django.db import models


class StatusModel(models.TextChoices):
    SUBMITTED = 'Submitted'
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    APPROVED = 'Approved'