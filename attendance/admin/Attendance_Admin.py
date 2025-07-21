from django.contrib import admin
from core.admin import BaseAdmin
from attendance.models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(BaseAdmin):
    list_display = ('shift', 'date', 'check_in_time', 'check_out_time', 'status')
    search_fields = ('worker', 'date')
    list_filter = ('worker', 'check_in_time', 'check_out_time', 'date')