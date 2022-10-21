from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<str:app_key>/<str:app_secret>/', consumers.MyConsumer.as_asgi())
]