from django.contrib import admin
from audit.models import AuditLog
from core.admin import BaseAdmin


@admin.register(AuditLog)
class AuditAdmin(BaseAdmin):
    list_display = ('user', 'action', 'ip_address')
    search_fields = ('user')
    list_filter = ('user', 'action', 'ip_address')