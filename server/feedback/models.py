from django.db import models


class Feedback(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )
    email = models.EmailField(
        verbose_name='Почта',
        max_length=255,
    )
    message = models.TextField(
        verbose_name='Сообщение',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    is_check = models.BooleanField(
        verbose_name='Проверено?',
        default=False
    )

    class Meta:
        verbose_name = '"обратная связь"'
        verbose_name_plural = 'Обратная связь'

    def __str__(self) -> str:
        return f'Обратная связь от {self.name} [{self.created_at}]'


