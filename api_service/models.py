from django.db import models
from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return list((x.name, x.value) for x in cls)


class BasketTypes(BaseEnum):
    REVIEW = 'review'
    CORRECT = 'correct'
    BLOCKED = 'blocked'


class Messages(models.Model):
    user_id = models.IntegerField('User')
    message = models.CharField('Message', max_length=255)
    status = models.CharField('Status', max_length=255, default=BasketTypes.REVIEW.name)
