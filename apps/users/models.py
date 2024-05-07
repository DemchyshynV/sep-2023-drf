from django.db import models

from core.models import BaseModel


class UserModel(BaseModel):
    class Meta:
        db_table = 'users'

    name = models.CharField(max_length=20)
    age = models.IntegerField()
