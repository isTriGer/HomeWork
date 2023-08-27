from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=128, verbose_name='заголовок')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auction = models.BooleanField('торг', help_text='отметьте, если уместен торг')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

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
