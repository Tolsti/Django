from django.shortcuts import render
from players.models import Team


def list_teams(request):
    template_name = 'players/teams_list.html'

    teams_query = Team.objects.prefetch_related('tournaments', 'players').all()

    context = {
        'teams': teams_query
    }

    return render(request, template_name, context)
