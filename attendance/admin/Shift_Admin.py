from django.contrib import admin
from core.admin import BaseAdmin
from attendance.models import ShiftModel


@admin.register(ShiftModel)
class ShiftAdmin(BaseAdmin):
    list_display = ('shift_name', 'start_time', 'end_time', 'break_duration', 'overtime_rate')
    search_fields = ('shift_name')
    list_filter = ('shift_name', 'start_time', 'end_time', 'break_duration', 'overtime_rate')