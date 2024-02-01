from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Album, AlbumImage


admin.site.empty_value_display = 'Не задано'


# class AlbumImageInLine(admin.TabularInline):
#     model = AlbumImage
#     extra = 1
#     readonly_fields = ('get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: contain" />')
#
#     get_image.short_description = 'Изображение'
#
#
# @admin.register(Album)
# class AlbumAdminPanel(admin.ModelAdmin):
#     fields: tuple[str] = ('name', 'banner', 'get_banner', 'description', 'images')
#     readonly_fields: tuple[str] = ('get_banner',)
#     list_display: tuple[str] = ('name', 'get_banner')
#     search_fields: tuple[str] = ('name',)
#     filter_horizontal: tuple[str] = ('images',)
#     inlines: tuple = (AlbumImageInLine,)
#
#     def get_banner(self, obj):
#         if obj.banner:
#             return mark_safe(f'<img src="{obj.banner.url}" width="50" height="50" style="object-fit: contain" />')
#         return None
#
#     get_banner.short_description = 'Изображение'
#
#
# @admin.register(AlbumImage)
# class AlbumImgAdminPanel(admin.ModelAdmin):
#     list_display: tuple[str] = ('title', 'album', 'get_image')
#     search_fields: tuple[str] = ('title', 'album')
#     readonly_fields: tuple[str] = ('get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: contain" />')
#
#     get_image.short_description = 'Изображение'
