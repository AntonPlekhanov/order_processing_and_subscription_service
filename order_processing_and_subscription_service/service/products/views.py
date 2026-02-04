from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer

import os
import requests


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save()
        try:
            telegram_id = order.user.telegram_id
            if telegram_id:
                TOKEN = os.getenv('TOKEN')
                if TOKEN:
                    requests.post(
                        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                        json={
                            "chat_id": telegram_id,
                            "text": "Вам пришёл новый заказ!"
                        },
                        timeout=3
                    )
        except:
            pass