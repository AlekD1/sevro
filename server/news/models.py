from django.db import models

from mixins.path_mixins import make_dir_for_news_images as new_path_images


class News(models.Model):
    """
    Данная модель описывает новости. Имеются такие поля
    как заголовок, изображение (баннер), внутренний контент,
    тэг и дата создания записи. Объект возвращается в
    формате: "Соц.сеть Название: Ссылка".
    """
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
        db_index=True
    )
    description = models.CharField(
        verbose_name='Краткое описание для карточки',
        max_length=255,
        db_index=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=new_path_images
    )
    content = models.TextField(
        verbose_name='Содержание'
    )
    tags = models.ManyToManyField(
        verbose_name='Теги',
        to='Tag',
        db_index=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name: str = 'Новость'
        verbose_name_plural: str = 'Новости'

    def __str__(self) -> str:
        return f'Новость: {self.title}'


class Tag(models.Model):
    """Данная модель описывает отдельный тег."""
    title = models.CharField(
        verbose_name='Название тега',
        max_length=255,
    )

    class Meta:
        verbose_name: str = 'Тег'
        verbose_name_plural: str = 'Теги'

    def __str__(self) -> str:
        return self.title
