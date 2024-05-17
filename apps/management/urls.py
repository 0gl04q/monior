from django.urls import path

from apps.management import views as v

urlpatterns = [
    path('', v.OrderListView.as_view(), name='order_list'),
    path('create/', v.OrderCreateView.as_view(), name='order_create'),
    path('<uuid:order_id>/', v.CardListView.as_view(), name='card_list'),
]
