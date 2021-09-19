from django.shortcuts import render
from players.models import Player


def list_players(request):
    template_name = 'players/players_list.html'

    players = Player.objects.all()
    players_first_four = Player.objects.filter(id__lt=4)
    players_after_four = Player.objects.filter(id__gt=4)
    players_only_five = Player.objects.all()[:5]
    players_only_five_revers = Player.objects.all().order_by('-id')[:5]

    filter_name = request.GET.get('name')
    exclude_name = request.GET.get('exclude_name')
    players_filter_name = Player.objects.all()
    if filter_name:
        players_filter_name = players_filter_name.filter(name__icontains=filter_name)
    if exclude_name:
        players_filter_name = players_filter_name.exclude(name__icontains=exclude_name)

    context = {
        'players': players,
        'players_first_four': players_first_four,
        'players_after_four': players_after_four,
        'players_only_five': players_only_five,
        'players_only_five_revers': players_only_five_revers,
        'players_filter_name': players_filter_name,
    }
    return render(request, template_name, context)
