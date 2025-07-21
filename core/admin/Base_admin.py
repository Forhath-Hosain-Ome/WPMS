from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):
    list_per_page = 25
    search_help_text = "Use this field to search by keyword"