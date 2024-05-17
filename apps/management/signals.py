from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.management.models import Card


@receiver(pre_save, sender=Card)
def add_real_price(sender, instance: Card, **kwargs):
    instance.real_price = instance.price - instance.bonus - instance.promo
