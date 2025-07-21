from django.contrib import admin
from attendance.models import LeaveModel, Attendance, ShiftModel, WorkShift
# Register your models here.

admin.site.register(LeaveModel)
admin.site.register(Attendance)
admin.site.register(ShiftModel)
admin.site.register(WorkShift)

