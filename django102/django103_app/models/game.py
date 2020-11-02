from django.db import models

# Create your models here.
from django103_app.models.player import Player


class GameManager(models.Manager):
    def all_with_players_count(self):
        games = self.all() \
            .annotate(players_count=models.Count('players'))
        return games


class Game(models.Model):
    objects = GameManager()

    EASY = 1
    MEDIUM = 2
    HARD = 3

    DIFFICULTY_LEVEL_CHOICES = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    )

    name = models.CharField(max_length=20, blank=False, default='')
    level_of_difficulty = models.IntegerField(
        blank=False,
        choices=DIFFICULTY_LEVEL_CHOICES,
        default=MEDIUM,
    )
    players = models.ManyToManyField(Player)

    def __str__(self):
        return f'{self.name}'
