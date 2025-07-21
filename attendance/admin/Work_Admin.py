from django.contrib import admin
from core.admin import BaseAdmin
from attendance.models import WorkShift


@admin.register(WorkShift)
class WorkAdmin(BaseAdmin):
    list_display = ('worker', 'shift', 'assignment_date', 'is_active')
    search_fields = ('worker', 'shift')
    list_filter = ('worker', 'shift', 'assignment_date')