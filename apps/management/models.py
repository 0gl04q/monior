import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_close=False)


class Order(models.Model):
    """ Модель заявки поиска"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(verbose_name='Искатель', to=User, on_delete=models.CASCADE, related_name='orders')
    query = models.CharField(verbose_name='Поисковой запрос', max_length=1000)
    created = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    last_search = models.DateTimeField(verbose_name='Время последнего обновления', auto_now=True)
    closed = models.DateTimeField(verbose_name='Время закрытия', null=True, blank=True)

    objects = models.Manager()
    active = ActiveManager()

    is_close = models.BooleanField(verbose_name='Открыт/Закрыт', default=False)

    class Meta:
        ordering = ('-created', 'is_close')
        verbose_name = 'Заявка поиска'
        verbose_name_plural = 'Заявки поиска'

    def __str__(self):
        return f'{self.query}'

    def get_success_url(self):
        return reverse('card_list', args=(self.id,))


class Card(models.Model):
    """ Класс карточки товара """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(verbose_name='Заявка', to=Order, on_delete=models.CASCADE, related_name='cards')
    name = models.CharField(verbose_name='Наименование', max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=9, decimal_places=2)
    bonus = models.IntegerField(verbose_name='Бонус', default=0)
    promo = models.IntegerField(verbose_name='Промокод', default=0)
    photo = models.URLField(verbose_name='Ссылка на фотографию')
    link = models.URLField(verbose_name='Ссылка на товар')

    real_price = models.DecimalField(verbose_name='Итоговая сумма', max_digits=9, decimal_places=2, blank=True)

    class Meta:
        ordering = ('real_price',)
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товара'

    def __str__(self):
        return f'{self.name}, итого: {self.real_price}'
