from django.db import models
from workers.models import WorkerModel
from accounts.models import UserModel

class PerformanceReviewModel(models.Model):
    worker = models.ForeignKey(WorkerModel, on_delete=models.SET_NULL, related_name='name', null=True)
    review_date = models.DateField(auto_now=True)
    reviewed_by = models.OneToOneField(UserModel, on_delete=models.SET_NULL, limit_choices_to={'role__in': ['ADMIN', 'HR', 'SUPERVISOR']}, null=True)
    kpi_score = models.PositiveBigIntegerField()
    comments = models.TextField(blank=True)
    overall_rating = models.DecimalField(max_digits=1, decimal_places=1)

    class Meta:
        verbose_name = 'Performance Review'
        verbose_name_plural = 'Performance Reviews'
        ordering = ['-review_date']

    def __str__(self):
        return f"Review for {self.worker} on {self.review_date}"