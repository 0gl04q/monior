import uuid
from rest_framework import serializers

from apps.management.models import Card, Order


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = ('id',)

    def to_internal_value(self, data):
        if 'order' in data:
            try:
                data['order'] = uuid.UUID(data['order'])
            except ValueError:
                raise serializers.ValidationError({"order": "Invalid UUID format."})

        return super().to_internal_value(data)


class CardListSerializer(serializers.Serializer):
    cards_list = CardSerializer(many=True)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'query')
