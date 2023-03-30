from django.db import models
from django.conf import settings


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField("Название", max_length=30, blank=False)
    message = models.CharField("сообщение", max_length=1000, blank=False)

    def __str__(self):
        return f"{self.title} - {self.author.username}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class Reviwes(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null=True)
    text = models.TextField("Сообщение", max_length=300)
    parents = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    blog = models.ForeignKey(Blog, verbose_name="Блог", on_delete=models.SET_NULL, null=True, related_name="reviews")

    def __str__(self):
        return f"{self.author.username} - {self.blog.title}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"