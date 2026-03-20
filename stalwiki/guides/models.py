from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name

class Guide(models.Model):
    name = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    tags = models.ManyToManyField(Tag, verbose_name='Тэг')

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководства'

    def __str__(self):
        return f'{self.user.username} - {self.name}'
