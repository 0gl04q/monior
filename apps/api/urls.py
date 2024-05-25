from django.urls import path
from apps.api.views import CardList, OrderDetail

urlpatterns = [
    path('order/<uuid:pk>/', OrderDetail.as_view(), name='order_detail_api'),
    path('cards/<uuid:order_id>/', CardList.as_view(), name='card_list_api')
]
