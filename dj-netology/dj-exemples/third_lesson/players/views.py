from django.shortcuts import render

from players.models import Player


def list_players(request):
    template_name = 'players/players_list.html'

    players = Player.objects.all()

    context = {
        'players': players
    }
    return render(request, template_name, context)
