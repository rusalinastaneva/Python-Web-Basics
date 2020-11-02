from django.db import models


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.description} {self.is_done}'
