from django.urls import path
from . import views, roomViews, deviceView

urlpatterns = [
    # path('', views.index, name='index'),
    path('get_app/', views.get_app, name='get_app'),

    # ROOM VIEWS
    path('rooms/', roomViews.rooms, name='rooms'),
    path('addRoom/', roomViews.addRoom, name='addRoom'),
    path('deleteRoom/<int:roomId>', roomViews.deleteRoom, name='deleteRoom'),

    # DEVICE VIEWS
    path('devices/', deviceView.devices, name='devices'),
    path('addDevice/', deviceView.addDevice, name='addDevice'),
    path('deleteDevice/<int:deviceId>', deviceView.deleteDevice, name='deleteDevice'),
]