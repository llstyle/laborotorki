from django.db import models
from django.conf import settings

# Create your models here.
class Client (models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    GENDER_CHOICES = (
        ("Fm", "Female"),
        ("Ml", "Male")
    )

    gender = models.CharField(max_length=9,
                             choices=GENDER_CHOICES,
                             default="Ml")

    dateOfBirth = models.DateField("Дата выхода", auto_now_add=False, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.id}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

