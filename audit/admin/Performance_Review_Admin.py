from django.contrib import admin
from audit.models import PerformanceReviewModel
from core.admin import BaseAdmin


@admin.register(PerformanceReviewModel)
class PerformanceAdmin(BaseAdmin):
    list_display = ('worker', 'review_date', 'reviewed_by', 'kpi_score', 'overall_rating')
    search_fields = ('worker', 'kpi_score', 'overall_rating')
    list_filter = ('worker', 'review_date', 'reviewed_by', 'kpi_score', 'overall_rating')