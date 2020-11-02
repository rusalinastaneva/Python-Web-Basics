from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView

from django103_app.models.game import Game
from django103_app.models.player import Player
from django103_app.models.person import Person


# Create your views here.
def index(request):
    users = User.objects.all()
    games = Game.objects.all()

    context = {
        'users_list': users,
        'games_list': games,
    }
    return render(request, 'index.html', context)


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'

    # Sorting games by name in asc order
    queryset = Game.objects.all().order_by('name')


def create_game(request):
    game = Game(
        name='Video',
        level_of_difficulty=Game.MEDIUM,
    )
    game.save()
    return redirect('index')

