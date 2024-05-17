from django.shortcuts import render
from django.views.generic import ListView


class OrderListView(ListView):
    template_name = 'management/order_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Заявки на поиск'
        return context
