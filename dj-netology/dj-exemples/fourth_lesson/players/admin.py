from django.contrib import admin
from players.models import Team, Player, Tournament


class TournamentsInline(admin.TabularInline):
    model = Tournament.teams.through
    extra = 3


class PlayerAdmin(admin.ModelAdmin):
    pass


class TeamAdmin(admin.ModelAdmin):
    inlines = (TournamentsInline,)


class TournamentAdmin(admin.ModelAdmin):
    inlines = (TournamentsInline,)


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Tournament, TournamentAdmin)
