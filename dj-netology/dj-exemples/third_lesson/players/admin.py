from django.contrib import admin

from players.models import Player, Team


class TeamAdmin(admin.ModelAdmin):
    pass


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'team', 'team')


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
