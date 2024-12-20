from django.db import models
from django.conf import settings

class lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(max_length=255, verbose_name='Описание')
    preview = models.ImageField(upload_to='lesson_previews/')
    link_video = models.URLField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name


class course(models.Model):
    id = models.AutoField(primary_key=True)  # Поле id с автоинкрементом
    name = models.CharField(max_length=255, verbose_name='Наименование')
    preview = models.ImageField(upload_to='previews/')
    description = models.TextField(max_length=255, verbose_name='Описание')
    lessons = models.ManyToManyField(lesson, related_name='courses')  # Связь ManyToMany с Уроком
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

