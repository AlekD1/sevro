from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from mixins.path_mixins import (
    make_dir_for_project_banner as new_project_path_banner,
    make_dir_for_project_images as new_project_path_images,
    make_dir_for_partner_image as new_partner_path_image
)


class HomeSlider(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='home-slider/banners/%Y-%m-%d',
    )

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннера'

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    """
    Данная модель описывает проекты. Имеются такие поля,
    как заголовок, баннер, внутренний контент и изображения.
    Объект возвращается в формате: "Проект: Заголовок"
    """
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
        db_index=True
    )
    banner = models.ImageField(
        verbose_name='Изображение',
        upload_to=new_project_path_banner
    )
    content = models.TextField(
        verbose_name='Содержание'
    )
    images = models.ManyToManyField(
        verbose_name='Изображения',
        to='ProjectImage',
        blank=True,
        related_name='project_images',
        default=None
    )
    created_at = models.DateField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name: str = 'Проект'
        verbose_name_plural: str = 'Проекты'

    def __str__(self):
        return f'Проект: {str(self.title)}'


class QA(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
    )
    value = models.TextField(
        verbose_name='Значение'
    )

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопрос-ответ'

    def __str__(self) -> str:
        return self.title


class Document(models.Model):
    """
    Данная модель описывает документы. Имеются такие поля,
    как название документа, файл и дата создания документа.
    Объект возвращается в формате: "Документ: Название"
    """
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    file = models.FileField(
        upload_to='secondary/documents/%Y-%m-%d',
        verbose_name='Файл'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name: str = 'Документ'
        verbose_name_plural: str = 'Документы'
        ordering: tuple[str] = ('created_at',)

    def __str__(self) -> str:
        return f'Документ: {self.title}'


class Statistic(models.Model):
    """Данная модель описывает статистику."""
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    value = models.CharField(
        verbose_name='Значение',
        max_length=255
    )
    position = models.IntegerField(
        verbose_name='Позиция',
        blank=True,
        null=True,
        default=0,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name: str = 'Статистика'
        verbose_name_plural: str = 'Статистики'

    def __str__(self) -> str:
        return self.title


class ProjectImage(models.Model):
    """
    Данная модель описывает отдельную фотографию проекта. Имеются
    такие поля как название проекта, сам проект и его фотографии.
    Объект возвращается в формате: "Изображение: Название_фото"
    """
    title = models.CharField(
        verbose_name='Название',
        max_length=255,
    )
    project = models.ForeignKey(
        verbose_name='Проект',
        to='Project',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=new_project_path_images,
    )

    class Meta:
        verbose_name: str = 'Изображение проекта'
        verbose_name_plural: str = 'Изображения проектов'

    def __str__(self) -> str:
        return f'Изображение: {str(self.title)}'


class Contact(models.Model):
    TYPE = (
        ('vk', 'VK'),
        ('telegram', 'Telegram'),
        ('phone', 'Телефон'),
        ('email', 'Почта'),
        ('join', 'Вступить'),
    )

    type = models.CharField(max_length=255, choices=TYPE, verbose_name='Тип', unique=True)
    value = models.CharField(max_length=255, verbose_name='Значение')

    class Meta:
        verbose_name = 'Контакт РСО'
        verbose_name_plural = 'Контакты РСО'

    def __str__(self) -> str:
        return f'[{self.type}] {self.value}'


@receiver(post_save, sender=ProjectImage)
def project_images_handler(instance: ProjectImage, **kwargs) -> None:
    """
    Данный обработчик реагирует на сигнал 'post_save' и добавляет
    объект instance в указанный у него проект (поле M2M).
    """
    if instance.project is not None:
        project = Project.objects.get(pk=instance.project.pk)
        project.images.add(instance)


@receiver(m2m_changed, sender=Project.images.through)
def m2m_handler(instance: Project, **kwargs) -> None:
    """
    Данный обработчик реагирует на сигналы 'pre_remove' и 'post_add'.
    При pre_remove проходится по каждому объекту и изменяет
    поле project (ForeignKey) на значение None (Null)
    При post_add проходится по каждому объекту и устанавливает
    в поле project (ForeignKey) объект привязанного альбома (Album).
    """
    action: str = kwargs.get('action')
    if action == 'pre_remove':
        for image_id in kwargs.get('pk_set'):
            album_image: ProjectImage = ProjectImage.objects.get(id=image_id)
            album_image.album = None
            album_image.save()
    if action == 'post_add':
        print(instance)
        for image_id in kwargs.get('pk_set'):
            album_image: ProjectImage = ProjectImage.objects.get(id=image_id)
            album_image.album = instance
            album_image.save()


class Partner(models.Model):
    name = models.CharField(
        verbose_name='Именование',
        max_length=100
    )
    image = models.ImageField(
        verbose_name='Партнер',
        upload_to=new_partner_path_image
    )
    link = models.URLField(
        verbose_name='Ссылка'
    )

    class Meta:
        verbose_name = 'партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self) -> str:
        return self.name
