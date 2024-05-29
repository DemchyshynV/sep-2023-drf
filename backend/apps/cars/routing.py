from django.urls import path

from .consumers import CarConsumer

websocket_urlpatterns = [
    path('', CarConsumer.as_asgi())
]
