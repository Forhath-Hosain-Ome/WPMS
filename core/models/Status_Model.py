from django.db import models


class StatusModel(models.TextChoices):
    SUBMITTED = 'Submitted'
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    APPROVED = 'Approved'

class AttandanceStatus(models.TextChoices):
    PRESENT = 'Present'
    ABSENT = 'Absent'
    LATE = 'Late'
    ON_LEAVE = 'On Leave'