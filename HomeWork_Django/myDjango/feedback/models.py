from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
