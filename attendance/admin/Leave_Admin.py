from django.contrib import admin
from core.admin import BaseAdmin
from attendance.models import LeaveModel, Attendance, ShiftModel, WorkShift
# Register your models here.

@admin.register(LeaveModel)
class LeaveModel(BaseAdmin):
    list_display = ('worker.username', 'leave_type', 'start_date', 'end_date', 'status', 'approved_by')
    search_fields = ('worker.username', 'approved_by')
    list_filter = ('leave_type', 'start_date', 'end_date', 'status')

admin.site.register(Attendance)
admin.site.register(ShiftModel)
admin.site.register(WorkShift)