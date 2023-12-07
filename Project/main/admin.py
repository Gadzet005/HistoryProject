from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from main.models import Factory, Picture, Article


class PicturesInline(admin.TabularInline):
    model = Picture
    extra = 0


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    fields = ("name", "description", "image", "lat_coord", "long_coord")
    list_display = ("name",)
    inlines = (PicturesInline,)


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    fields = ("title", "text", "next")
    list_display = ("title",)
    summernote_fields = ("text",)
