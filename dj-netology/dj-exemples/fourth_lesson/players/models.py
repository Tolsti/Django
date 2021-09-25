from django.db import models


class Player(models.Model):
    name = models.TextField()
    team = models.ForeignKey(
        'Team',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='players'
    )

    def __str__(self):
        return f'{self.id}: {self.name}'


class Team(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.name}'


class Tournament(models.Model):
    name = models.TextField()
    teams = models.ManyToManyField(
        Team,
        related_name='tournaments')

    def __str__(self):
        return f'{self.id}: {self.name}'
