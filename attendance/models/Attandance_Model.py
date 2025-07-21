from django.db import models
from workers.models import WorkerModel
from attendance.models import Shift
from core.models import AttandanceStatus
from datetime import timedelta

class Attendance(models.Model):
    worker = models.ForeignKey(WorkerModel, on_delete=models.CASCADE, related_name='attendances')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(auto_now_add=True)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=AttandanceStatus, max_length=10)

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        ordering = ['-date']

    def __str__(self):
        return f"{self.worker} - {self.date} - {self.status}"

    @property
    def worked_hours(self):
        if self.check_in_time and self.check_out_time:
            duration = self.check_in_time - self.check_out_time
            return duration.seconds()/3600
        return 0
    @property
    def payable_hours(self):
        if self.shift:
            break_hours = self.shift.break_duration.seconds()/3600
            return max(self.worked_hours - self.break_hours, 0)
        return self.worked_hours
    @property
    def overtime_hours(self):
        if self.check_in_time and self.check_out_time:
            if not (self.check_in_time and self.check_out_time):
                return 0
        scheduled_end = self.check_in_time.replace(
            hour=self.shift.end_time.hour,
            minute=self.shift.end_time.minute,
            second=0,
            microsecond=0
    )

        if self.shift.end_time < self.shift.start_time:
            scheduled_end += timedelta(days=1)

        if self.check_out_time <= scheduled_end:
            return 0

        overtime = self.check_out_time - scheduled_end
        return round(overtime.total_seconds() / 3600, 2)