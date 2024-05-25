from django.db.models import F
from django.utils import timezone

from datetime import timedelta

from monitor.celery import app
from apps.management.models import Order
from parser_market.scraper import Scraper


@app.task
def start_search_cards(query, order_id):
    Scraper(query, order_id)


@app.task
def search_all_active_order():
    interval = timedelta(minutes=5)

    orders = Order.active.annotate(
        diff_last_search=timezone.now()-F('last_search')
    ).filter(diff_last_search__gt=interval)

    for order in orders:
        
        Scraper(order.query, order.id)
        order.save()
