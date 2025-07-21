from django.contrib import admin
from core.admin import BaseAdmin
from attendance.models import LeaveModel


@admin.register(LeaveModel)
class LeaveAdmin(BaseAdmin):
    list_display = ('worker', 'leave_type', 'start_date', 'end_date', 'status', 'approved_by')
    search_fields = ('worker', 'approved_by')
    list_filter = ('leave_type', 'start_date', 'end_date', 'status')