from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from apps.management.models import Card, Order
from apps.api.serializers import CardListSerializer, CardSerializer, OrderSerializer


class CardList(APIView):

    def get(self, request, order_id, format=None):
        cards = Card.objects.filter(order__id=order_id)
        if cards.exists():
            serializer = CardSerializer(cards, many=True)
            return Response(serializer.data)
        raise Http404(f'Not found: order__id={order_id}')

    def post(self, request, order_id, format=None):
        serializer = CardSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id, format=None):
        try:
            order = Order.active.get(id=order_id)
        except Order.DoesNotExist:
            raise Http404(f'Not found: order__id={order_id}')

        order.cards.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderDetail(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
