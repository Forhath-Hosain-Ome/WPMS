from django.contrib import admin
from .models import UserModel
# Register your models here.

@admin.register(UserModel)
class UserModel(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'linked_worker')
    search_fields = ('username', 'email')
    list_filter = ('role',)
    list_per_page = 25
    search_help_text = "Use this field to search by keyword"