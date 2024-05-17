from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from apps.management.models import Order, Card


@receiver(pre_save, sender=Card)
def add_real_price(sender, instance: Card, **kwargs):
    instance.real_price = instance.price - instance.bonus - instance.promo


@receiver(post_save, sender=Order)
def lower_query(sender, instance: Order, created, **kwargs):
    if created:
        instance.query = instance.query.lower()
        instance.save()
