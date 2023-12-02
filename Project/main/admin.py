from django.contrib import admin

from main.models import Factory, Picture


class PicturesInline(admin.TabularInline):
    model = Picture
    extra = 0


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    fields = ("name", "description", "lat_coord", "long_coord")
    list_display = ("name",)
    inlines = (PicturesInline,)
