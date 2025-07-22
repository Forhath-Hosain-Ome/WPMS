from django.db import models
from django.utils import timezone

class AttendanceManager(models.Manager):
    def for_date(self, date=None):
        if date is None:
            date = timezone.now().date()
        return self.filter(date=date)

    def present_workers(self, date=None):
        return self.for_date(date).filter(status='PRESENT')

    def absent_workers(self, date=None):
        return self.for_date(date).filter(status='ABSENT')

    def for_worker(self, worker, start_date=None, end_date=None):
        qs = self.filter(worker=worker)
        if start_date and end_date:
            qs = qs.filter(date__range=(start_date, end_date))
        return qs