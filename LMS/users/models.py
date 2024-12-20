from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text='Добавьте ваш аватар'
    )
    phone = models.CharField(
        max_length=30,
        verbose_name='Телефон',
        blank=True,
        null=True,
        help_text='Введите номер телефона'
    )
    country = models.CharField(
        max_length=35,
        verbose_name='Страна',
        blank=True,
        null=True,
        help_text='Введите страну, откуда вы'
    )

    token = models.CharField(
        max_length=100,
        verbose_name='Token',
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа')
    course_or_lesson = models.CharField(max_length=255, verbose_name='Оплаченный курс или урок')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежы'

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.payment_method}"
