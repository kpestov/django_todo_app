from django.db import models
from django.core.validators import MinLengthValidator


class Todo(models.Model):
    title = models.CharField(max_length=150)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
