from django.db import models

# Create your models here.
from app.validators import validate_does_contain_spaces


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=(validate_does_contain_spaces,)
    )
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField()


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
