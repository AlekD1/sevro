from django.contrib import admin

from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdminPanel(admin.ModelAdmin):
    list_display: tuple[str] = ('name', 'created_at', 'is_check')
    search_fields: tuple[str] = ('name', 'created_at', 'is_check')
