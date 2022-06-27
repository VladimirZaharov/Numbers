from rest_framework.serializers import HyperlinkedModelSerializer

from orders.models import Order


class OrderModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
