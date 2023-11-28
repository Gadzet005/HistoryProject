from django.contrib import admin

from main.models import Factory, Picture


class PicturesInline(admin.TabularInline):
    model = Picture
    extra = 0


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    fields = ("name", "description")
    list_display = ("name",)
    inlines = (PicturesInline,)
