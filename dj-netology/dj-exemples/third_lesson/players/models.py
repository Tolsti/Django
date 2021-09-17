from django.db import models


class Player(models.Model):
    name = models.TextField

    def __str__(self):
        return f'{self.id}: {self.name}'


class Team(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.name}'
