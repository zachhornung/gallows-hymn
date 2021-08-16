from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Item
from .permissions import IsOwnerOrReadOnly
from .serializers import ItemSerializer


class ItemList(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
