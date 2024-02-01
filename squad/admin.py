from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment

from squad.models import Squad, Figure, Position, Direction

admin.site.empty_value_display = 'Не задано'

admin.site.unregister(Attachment)

@admin.register(Squad)
class SquadAdminPanel(SummernoteModelAdmin):
    fieldsets = (
        ('Главная информация', {
            'fields': ('name', 'direction', 'create'),
        }),
        ('Доп.информация', {
            'fields': (
                ('get_main_image', 'main_image'),
                'figures', 'description', 'content'
            )
        }),
        ('Контакты', {
            'fields': ('vk', 'telegram', 'email')
        }),
        # ('Альбомы отряда', {
        #     'fields': ('albums',)
        # })
    )
    readonly_fields: tuple[str] = ('get_main_image',)
    list_display: tuple[str] = ('name', 'direction', 'create', 'get_main_image')
    search_fields: tuple[str] = ('direction', 'name')
    filter_horizontal: tuple[str] = ('figures', 'albums')
    summernote_fields: tuple[str] = ('content',)

    def get_main_image(self, obj):
        if obj.main_image:
            return mark_safe(f'<img src="{obj.main_image.url}" width="50" height="50" style="object-fit: contain" />')
        return None

    get_main_image.short_description = 'Изображение'

@admin.register(Figure)
class FigureAdminPanel(admin.ModelAdmin):
    fieldsets = (
        ('Главная информация', {
            'fields': ('position', 'name', 'on_main'),
        }),
        ('Доп.информация', {
            'fields': (('get_image', 'image'),
                        'phone', 'email')
        })
    )
    list_display: tuple[str] = ('name', 'position', 'get_image')
    readonly_fields: tuple[str] = ('get_image',)
    search_fields: tuple[str] = ('name', 'position')
    list_editable: tuple[str] = ('position',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="60" height="50" style="object-fit: contain" />')

    get_image.short_description = 'Фотография'


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display: tuple[str] = ('id', 'position_type')


@admin.register(Direction)
class DirectionAdminPanel(SummernoteModelAdmin):
    fieldsets = (
        ('Главная информация', {
            'fields': ('name', 'description'),
        }),
        ('Доп.информация', {
            'fields': (
                ('get_image', 'main_image'),
                ('get_icon', 'icon'),
                'content',
            )
        })
    )
    readonly_fields: tuple[str] = ('get_image', 'get_icon')
    list_display: tuple[str] = ('name', 'get_image', 'get_icon')
    search_fields: tuple[str] = ('name', 'description')
    summernote_fields: tuple[str] = ('content',)

    def get_icon(self, obj):
        return mark_safe(f'<img src="{obj.icon.url}" width="60" height="50" style="object-fit: contain" />')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.main_image.url}" width="60" height="50" style="object-fit: contain" />')

    get_image.short_description = 'Изображение'
    get_icon.short_description = 'Иконка'
