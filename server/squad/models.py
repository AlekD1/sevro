from django.db import models

from mixins.path_mixins import make_dir_for_squad_main_image as new_path

class Squad(models.Model):
    """
    Модель отдельного отряда, в котором указаны
    дата создания, ключевые фигуры и направление отряда.
    Объект возвращается в формате: "[Направление] Название_отряда".
    Сортировка отрядов идет по направлению каждого из них.
    """
    name = models.CharField(
        verbose_name='Название отряда',
        max_length=255,
        db_index=True
    )
    main_image = models.ImageField(
        verbose_name='Основная фотография',
        upload_to=new_path,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    content = models.TextField(
        verbose_name='Контент'
    )
    albums = models.ManyToManyField(
        verbose_name='Альбомы',
        to='album.Album',
        blank=True,
        related_name='squad_albums',
        default=None
    )
    phone = models.CharField(
        verbose_name='Телефон отряда',
        max_length=30,
        null=True,
        blank=True,
        default=None
    )
    email = models.EmailField(
        verbose_name='Почта отряда',
        null=True,
        blank=True,
        default=None
    )
    vk = models.URLField(
        verbose_name='Группа "ВКонтакте"',
        null=True,
        blank=True,
        default=None
    )
    telegram = models.URLField(
        verbose_name='Группа "Телеграм"',
        null=True,
        blank=True,
        default=None
    )
    create = models.DateField(
        verbose_name='Дата создания'
    )
    figures = models.ManyToManyField(
        verbose_name='Ключевые фигуры',
        to='Figure',
        blank=True,
        related_name='squad_important_people',
        default=None
    )
    direction = models.ForeignKey(
        verbose_name='Направление отряда',
        to='Direction',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='squad'
    )

    class Meta:
        verbose_name: str = 'Отряд'
        verbose_name_plural: str = 'Отряды'
        ordering = ['direction__name']

    def __str__(self) -> str:
        """
        Метод возвращает название объекта
        в формате: "[Направление] Название_отряда".
        """
        return f'[{self.direction}] {self.name}'


class Figure(models.Model):
    """
    Модель отдельных руководящих лиц в отрядах
    с указанием их должности. Объект возвращается
    в формате: "[Должность] Имя_Фамилия".
    """
    name = models.CharField(
        verbose_name='ФИО человека',
        max_length=255,
        db_index=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='squads/important_people/%Y-%m-%d'
    )
    position = models.ForeignKey(
        verbose_name='Должность',
        to='Position',
        on_delete=models.SET_NULL,
        null=True,
        related_name='figures'
    )
    on_main = models.BooleanField(
        verbose_name='На главную?',
        default=False,
        blank=True
    )
    phone = models.CharField(
        verbose_name='Личный телефон',
        max_length=30,
        null=True,
        blank=True,
        default=None
    )
    email = models.EmailField(
        verbose_name='Личная почта',
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        verbose_name: str = 'Ключевая фигура'
        verbose_name_plural: str = 'Ключевые фигуры'


    def __str__(self) -> str:
        """
        Метод возвращает название объекта
        в формате: "[Должность] Имя_Фамилия".
        """
        return self.name


class Position(models.Model):
    """
    Данная модель описывает объект "Должность". Объекты не
    могут повторяться. Объект возвращается в формате: "Должность"
    """
    position_type = models.CharField(
        verbose_name='Позиция персонажа',
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name: str = 'Должность человека'
        verbose_name_plural: str = 'Должности людей'

    def __str__(self) -> str:
        """
        Метод возвращает название объекта
        в формате: "Должность".
        """
        return self.position_type


class Application(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=100
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )
    date = models.DateTimeField(
        verbose_name='Дата создания'
    )
    answered = models.BooleanField(
        verbose_name='Отвечено?',
        default=False,
        blank=True
    )

    class Meta:
        verbose_name: str = 'Заявление'
        verbose_name_plural: str = 'Заявления'

    def __str__(self) -> str:
        return f'[{self.date}] Заявление от {self.name}'


class Direction(models.Model):
    """
    Модель указывающая разновидности отрядов.
    Данная модель описывает разновидности направлений. Имеются
    такие поля как название направления, главное изображение,
    краткое описание, внутренний контент, ссылка на альбомы,
    ссылки на социальные сети. Объект возвращается в
    формате: "Альбом: Название_альбома". Объекты
    сортируются по названию направления.
    """
    name = models.CharField(
        verbose_name='Название направление',
        max_length=255,
        db_index=True
    )
    main_image = models.ImageField(
        verbose_name='Главное изображение',
        upload_to='direction/images/%Y-%m-%d',
    )
    description = models.TextField(
        verbose_name='Краткое описание'
    )
    content = models.TextField(
        verbose_name='Контент'
    )
    icon = models.ImageField(
        verbose_name='Иконка',
        upload_to='direction/icons',
        default=None,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name: str = 'Направление отряда'
        verbose_name_plural: str = 'Направления отрядов'
        ordering: tuple[str] = ('name',)

    def __str__(self) -> str:
        return self.name