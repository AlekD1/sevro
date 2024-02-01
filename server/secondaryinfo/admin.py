from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from secondaryinfo.models import HomeSlider, Project, ProjectImage, Document, Statistic, QA, Contact, Partner

# admin.site.register(HomeSlider)
admin.site.empty_value_display = 'Не задано'


@admin.register(HomeSlider)
class HomeSliderAdminPanel(admin.ModelAdmin):
    fieldsets = [
        ('Наименование', {
            'fields': (
                'title',
            ),
        }),
        ('Доп. информация', {
            'fields': ('get_image', 'image')
        })
    ]
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: contain" />')
        return None

    get_image.short_description = 'Изображение баннера'

# class ProjectImageInLine(admin.TabularInline):
#     model = ProjectImage
#     extra = 1
#     readonly_fields = ('get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: contain" />')
#
#     get_image.short_description = 'Изображение'


# @admin.register(Project)
# class ProjectAdminPanel(SummernoteModelAdmin):
#     fields: tuple[str] = (
#         'title',
#         'banner',
#         'get_banner',
#         'content',
#         'images',
#         'created_at'
#     )
#     list_display: tuple[str] = ('title', 'created_at', 'get_banner')
#     readonly_fields: tuple[str] = ('get_banner', 'created_at')
#     search_fields: tuple[str] = ('title', 'id', 'created_at')
#     ordering: tuple[str] = ('-id', 'title')
#     filter_horizontal: tuple[str] = ('images',)
#     inlines: tuple = (ProjectImageInLine,)
#     summernote_fields: tuple[str] = ('content',)
#
#     def get_banner(self, obj):
#         return mark_safe(f'<img src="{obj.banner.url}" width="60" height="50" style="object-fit: contain" />')
#
#     get_banner.short_description = 'Фотография'


@admin.register(Document)
class DocumentsAdminPanel(admin.ModelAdmin):
    list_display: tuple[str] = ('title', 'id', 'created_at')
    search_fields: tuple[str] = ('title', 'id', 'created_at')
    ordering: tuple[str] = ('-id', 'title')


@admin.register(Statistic)
class StatisticAdminPanel(admin.ModelAdmin):
    list_display: tuple[str] = ('title', 'value', 'position')
    search_fields: tuple[str] = ('title', 'value', 'position')
    ordering: tuple[str] = ('title', 'position')


@admin.register(QA)
class QAAdminPanel(admin.ModelAdmin):
    fieldsets = (
        ('Вопрос', {
            'fields': ('title',)
        }),
        ('Ответ', {
            'fields': ('value',)
        }),
    )
    list_display: tuple[str] = ('title', )
    search_fields: tuple[str] = ('title', )
    ordering: tuple[str] = ('title', )

@admin.register(Contact)
class ContactAdminPanel(admin.ModelAdmin):
    list_display: tuple[str] = ('type', )
    search_fields: tuple[str] = ('type', )
    ordering: tuple[str] = ('type', )


# @admin.register(ProjectImage)
# class ProjectImageAdminPanel(admin.ModelAdmin):
#     list_display: tuple[str] = ('title', 'get_image')
#     readonly_fields: tuple[str] = ('get_image',)
#     search_fields: tuple[str] = ('title',)
#     ordering: tuple[str] = ('project', 'title')
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: contain" />')
#
#     get_image.short_description = 'Изображение'




@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Главная информация', {
            'fields': ('name', 'link')
        }),
        ('Дополнительная информация', {
            'fields': ('get_image', 'image')
        }),
    )
    list_display = ('name', 'link', 'get_image')
    readonly_fields: tuple[str] = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: contain" />')
        return None

    get_image.short_description = 'Изображение'

