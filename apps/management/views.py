from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.management.models import Order, Card
from apps.management.forms import OrderModelForm

from parser_market.scraper import Scraper


class OrderCreateView(CreateView):
    form_class = OrderModelForm
    template_name = 'management/order_create.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание заявки'
        return context


class OrderListView(ListView):
    template_name = 'management/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.active.filter(author=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Заявки на поиск'
        return context


class CardListView(ListView):
    template_name = 'management/card_list.html'
    context_object_name = 'cards'

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return Card.objects.filter(order__id=order_id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        order_id = self.kwargs['order_id']
        context['order'] = Order.active.get(id=order_id)
        context['title'] = 'Карточки'
        return context
