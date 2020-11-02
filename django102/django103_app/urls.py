from django.urls import path

from django103_app.views import index, GamesListView, create_game

urlpatterns = [
    path('', index, name='index'),
    path('games/', GamesListView.as_view()),
    path('create_game/', create_game),
]