from django.contrib import admin
from .models import AuditLog, PerformanceReviewModel
# Register your models here.

admin.site.register(AuditLog)
admin.site.register(PerformanceReviewModel)