import uuid

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    """ Модель товара """

    id = models.UUIDField(primary_key=True)
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    """ Модель заявки поиска"""

    id = models.UUIDField(primary_key=True)
    product = models.ForeignKey(verbose_name='Товар', to=Product, on_delete=models.CASCADE, related_name='orders')
    author = models.ForeignKey(verbose_name='Искатель', to=User, on_delete=models.CASCADE, related_name='orders')
    query = models.CharField(verbose_name='Поисковой запрос', max_length=1000)
    created = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    closed = models.DateTimeField(verbose_name='Время закрытия', null=True)

    is_close = models.BooleanField(verbose_name='Открыт/Закрыт', default=False)

    class Meta:
        ordering = ('-created', 'is_close')
        verbose_name = 'Заявка поиска'
        verbose_name_plural = 'Заявки поиска'


class Card(models.Model):
    """ Класс карточки товара """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(verbose_name='Заявка', to=Order, on_delete=models.CASCADE, related_name='cards')
    name = models.CharField(verbose_name='Наименование', max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=9, decimal_places=2)
    bonus = models.IntegerField(verbose_name='Бонус', default=0)
    promo = models.IntegerField(verbose_name='Промокод', default=0)
    link = models.URLField(verbose_name='Ссылка на товар')

    real_price = models.DecimalField(verbose_name='Итоговая сумма', max_digits=9, decimal_places=2)

    class Meta:
        ordering = ('real_price',)
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товара'
