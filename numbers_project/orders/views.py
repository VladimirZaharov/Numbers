from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderModelSerializer


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
