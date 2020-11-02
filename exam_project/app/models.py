from django.db import models


# Create your models here.
from app.validators import validate_time_is_negative_or_zero


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    # Each field takes an optional first positional argument – a verbose name - Image URL
    image_url = models.URLField("Image URL")
    description = models.TextField()
    ingredients = models.CharField(max_length=250)
    time = models.IntegerField(
        "Time (Minutes)",
        validators=(validate_time_is_negative_or_zero, )
    )

    def ingredients_list(self):
        return self.ingredients.split(', ')

    def __str__(self):
        return f'{self.title}'

