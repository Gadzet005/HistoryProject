from django.contrib import admin

from main.models import Factory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    fields = ("title", "content")
    list_display = ("title",)
