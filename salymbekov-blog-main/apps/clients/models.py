from django.db import models


class Client(models.Model):
    name = models.CharField(
        max_length=256
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    phone_number = models.CharField(
        max_length=256
    )
    email = models.EmailField(
        max_length=256
    )

    def __str__(self) -> str:
        return self.name
    


# Create your models here.
