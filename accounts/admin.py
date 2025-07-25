from core.admin import BaseAdmin
from django.contrib import admin
from accounts.models import UserModel
# Register your models here.

@admin.register(UserModel)
class UserAdmin(BaseAdmin):
    list_display = ('username', 'email', 'role', 'linked_worker')
    search_fields = ('username', 'email')
    list_filter = ('role',)