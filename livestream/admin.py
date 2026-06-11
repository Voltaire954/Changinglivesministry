from django.contrib import admin
from .models import LiveStream


@admin.register(LiveStream)
class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "platform", "started_at")
    list_editable = ("is_active",)
