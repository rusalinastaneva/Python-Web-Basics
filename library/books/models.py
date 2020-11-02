from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerField(default=0)
    description = models.TextField(max_length=400, default='')
    author = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title} / {self.author}'