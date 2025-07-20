from django.db import models
from workers.models import WorkerModel
from accounts.models import UserModel

class PerformanceReviewModel(models.Model):
    worker = models.OneToOneField(WorkerModel, on_delete=models.CASCADE, related_name='name')
    review_date = models.DateField(auto_now=True)
    reviewed_by = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    kip_score = models.PositiveBigIntegerField()
    comments = models.TextField()
    overall_ratting = models.DecimalField()

    def __str__(self):
        return self.worker