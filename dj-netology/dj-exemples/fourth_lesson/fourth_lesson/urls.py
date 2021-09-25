from django.contrib import admin
from django.urls import path
from players.views import list_teams

urlpatterns = [
    path('teams/', list_teams, name='list-teams'),
    path('admin/', admin.site.urls),
]
