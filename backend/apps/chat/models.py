from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ChatModel(models.Model):
    class Meta:
        db_table = 'chat'

    body = models.CharField(max_length=255)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
