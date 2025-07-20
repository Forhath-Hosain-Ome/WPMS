from django.db import models

class Shift(models.Model):
    shift_name = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_duration = models.DurationField(help_text="Duration of breaks (e.g., 00:30:00 for 30 minutes)")
    overtime_rate = models.DecimalField(max_digits=3, decimal_places=2, help_text="Overtime pay rate per hour")

    class Meta:
        verbose_name = "Shift"
        verbose_name_plural = "Shifts"
        ordering = ['start_time']

    def __str__(self):
        return f"{self.shift_name} ({self.start_time} - {self.end_time})"