from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from mixins.path_mixins import (
    make_dir_for_album as new_path_banner,
    make_dir_for_album_images as new_path_images
)


class Album(models.Model):
    """
    Данная модель описывает альбом в целом. Имеются
    такие поля как название альбома, главное изображение (баннер),
    описание и ссылка на объект с фотографиями.
    Объект возвращается в формате: "Альбом: Название_альбома"
    """
    name = models.CharField(
        verbose_name='Название альбома',
        max_length=255,
        db_index=True
    )
    banner = models.ImageField(
        verbose_name='Главное изображение альбома',
        upload_to=new_path_banner,
        null=True,
        blank=True,
        default=None,
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    images = models.ManyToManyField(
        verbose_name='Изображения',
        to='AlbumImage',
        blank=True,
        related_name='album_images',
        default=None
    )

    class Meta:
        verbose_name: str = 'Альбом'
        verbose_name_plural: str = 'Альбомы'

    def __str__(self) -> str:
        return f'Альбом: {self.name}'


class AlbumImage(models.Model):
    """
    Данная модель описывает отдельную фотографию. Имеются
    такие поля как заголовок фото, альбом, сама фотография.
    Объект возвращается в формате: "Фотография: Заголовок_фото"
    """
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    album = models.ForeignKey(
        verbose_name='Альбом',
        to='Album',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=new_path_images,
    )

    class Meta:
        verbose_name: str = 'Изображение альбома'
        verbose_name_plural: str = 'Изображения альбомов'
        ordering: tuple[str] = ('album',)

    def __str__(self) -> str:
        return f'Фотография: {self.title}'


@receiver(post_save, sender=AlbumImage)
def album_images_handler(instance: AlbumImage, **kwargs) -> None:
    """
    Данный обработчик реагирует на сигнал 'post_save' и добавляет
    объект instance в указанный у него альбом (поле M2M).
    """
    if instance.album is not None:
        album = Album.objects.get(pk=instance.album.pk)
        album.images.add(instance)


@receiver(m2m_changed, sender=Album.images.through)
def m2m_handler(instance: Album, **kwargs) -> None:
    """
    Данный обработчик реагирует на сигналы 'pre_remove' и 'post_add'.
    При pre_remove проходится по каждому объекту и изменяет
    поле album (ForeignKey) на значение None (Null)
    При post_add проходится по каждому объекту и устанавливает
    в поле album (ForeignKey) объект привязанного альбома (Album).
    """
    action: str = kwargs.get('action')
    if action == 'pre_remove':
        for image_id in kwargs.get('pk_set'):
            album_image: AlbumImage = AlbumImage.objects.get(id=image_id)
            album_image.album = None
            album_image.save()
    if action == 'post_add':
        for image_id in kwargs.get('pk_set'):
            album_image: AlbumImage = AlbumImage.objects.get(id=image_id)
            album_image.album = instance
            album_image.save()