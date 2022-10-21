from django.db import models
import random

def room_key_generator():
    key = random.randint(100000,999999)
    if Rooms.objects.filter(roomId=key).exists():
        key = room_key_generator()
    return key

def item_key_generator():
    key = random.randint(100000,999999)
    if Items.objects.filter(itemId=key).exists():
        key = item_key_generator()
    return key

class Rooms(models.Model):
    roomName = models.CharField(max_length=50)
    espId = models.CharField(max_length=17, unique=True)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey('account.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.roomName

class Items(models.Model):
    roomId = models.ForeignKey('Rooms', related_name='roomInfo', on_delete=models.CASCADE)
    itemId = models.CharField(unique=True, max_length=6, default = item_key_generator, editable = False)
    itemType = models.CharField(max_length=10, blank=False, default='BULB')
    itemName = models.CharField(max_length=50, blank=False, default='')
    itemStatus = models.BooleanField(default=False)
    itemConnected = models.BooleanField(default=True)
    created_by = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.itemName