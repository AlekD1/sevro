from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from news.models import News, Tag


admin.site.empty_value_display = 'Не задано'


@admin.register(News)
class NewsAdminPanel(SummernoteModelAdmin):
    fields: tuple[str] = (
        'title',
        'description',
        'image',
        'get_image',
        'tags',
        'content',
        'created_at'
    )
    list_display: tuple[str] = ('title', 'created_at')
    search_fields: tuple[str] = ('title', 'tags', 'created_at')
    readonly_fields: tuple[str] = ('get_image', 'created_at')
    filter_horizontal: tuple[str] = ('tags',)
    summernote_fields: tuple[str] = ('content',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="200" height="200" style="object-fit: contain" />')

    get_image.short_description = 'Изображение'


@admin.register(Tag)
class TagAdminPanel(admin.ModelAdmin):
    list_display: tuple[str] = ('title', )
    search_fields: tuple[str] = ('title', )
