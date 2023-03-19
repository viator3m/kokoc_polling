from django.contrib.auth.models import AbstractUser
from django.db import models


COLOR = (
    ('white', 'Белый'),
    ('gray', 'Серый'),
    ('red', 'Красный'),
    ('gold', 'Золотой'),
)

STYLES = (
    ('white', 'Белый'),
    ('lightgray', 'Серый'),
    ('#FFC0CB', 'Розовый'),
    ('#90e3ff', 'Голубой'),
)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
    )
    background_color = models.CharField(
        max_length=16,
        choices=COLOR,
        default='white'
    )
    background_style = models.CharField(
        max_length=16,
        choices=STYLES,
        default='white'
    )
    money = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=('username', 'email'),
                name='unique_user'
            )
        ]

    def __str__(self):
        return self.username
