from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


class OnlineChatUsers(models.Model):
    online = models.ManyToManyField(User, null=True, blank=True)
    group_name = models.CharField("ИмяГруппы", max_length=50, null=True)
    class Meta:
        verbose_name = "Онлайн"
        verbose_name_plural = "Онлайн"

