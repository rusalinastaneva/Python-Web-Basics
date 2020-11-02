from django.core import validators
from django.db import models

from testing_app.validators import contains_only_digits


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(0),
            validators.MaxValueValidator(150),
        )
    )
    egn = models.CharField(
        max_length=10,
        validators=(
            validators.MinLengthValidator(10),
            validators.MaxLengthValidator(10),
            contains_only_digits,
        )
    )
