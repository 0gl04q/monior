from django.urls import path

from apps.management import views as v

urlpatterns = [
    path('', v.OrderListView.as_view(), name='order_list')
]
