from django.contrib import admin
from .models import PayrollModel
from core.admin import BaseAdmin
# Register your models here.

@admin.register(PayrollModel)
class PayrollAdmin(BaseAdmin):
    list_display = ('worker', 'base_salary', 'overtime_hour', 'generated_date')
    search_fields = ('worker', 'generated_date')
    list_filter = ('worker', 'base_salary', 'overtime_hour', 'generated_date')