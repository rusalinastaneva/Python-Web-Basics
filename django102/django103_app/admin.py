from django.contrib import admin

# Register your models here.
from django103_app.models.game import Game
from django103_app.models.player import Player


# Customizing the admin panel
class GameAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'players',
    )

admin.site.register(Game, GameAdmin)
admin.site.register(Player)


