from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

# Create your models here.

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField(max_length=128, verbose_name='заголовок', validators=[
        RegexValidator(regex=r'^\?', message='Заголовок не может начинаться с ?', inverse_match=True)])
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auction = models.BooleanField(verbose_name='торг', help_text='отметьте, если уместен торг')
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='изображение', upload_to='advertisements/')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self. create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: blood;">Сегодня в {}</span>', created_time
            )
        elif timezone.now().day - self.create_at.day == 1:
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: #d6c800; font-weight: blood;">Вчера в {}</span>', created_time
            )
        elif timezone.now().day - self.create_at.day == 2:
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: orange; font-weight: blood;">Позавчера в {}</span>', created_time
            )
        return self.create_at.strftime('%d.%m.%y')

    @admin.display(description='Дата Обновления')
    def updated_date(self):
        if self.update_at.date() == timezone.now().date():
            created_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: blood;">Сегодня в {}</span>', created_time
            )
        elif timezone.now().day - self.update_at.day == 1:
            created_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: #d6c800; font-weight: blood;">Вчера в {}</span>', created_time
            )
        elif timezone.now().day - self.update_at.day == 2:
            created_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: orange; font-weight: blood;">Позавчера в {}</span>', created_time
            )
        return self.update_at.strftime('%d.%m.%y')

    @admin.display(description='Картинка')
    def image_html(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 64px; max-height: 64px;">', url=self.image.url
            )

    class Meta:
        db_table = 'advertisements'


"""
Название (заголовок)
Описание
Цена 
Дата создания
Дата обновления
Уместен ли торг
"""
