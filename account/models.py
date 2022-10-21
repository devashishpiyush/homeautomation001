from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    app_key = models.UUIDField(default=uuid.uuid4, editable=False)
    app_secret = models.UUIDField(default=uuid.uuid4, editable=False)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
