from django.db import models
from accounts.models import Profile
from cards.models import City, Card, Disease
import random
# Create your models here.

class InfectionCard(models.Model):
    location = models.ForeignKey('game.CityNode', on_delete=models.CASCADE, null=True)
    is_discarded = models.BooleanField(default=False)
    index = models.IntegerField(null=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='infection_deck')

    class Meta:
        ordering = ['-index']

class DeckCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    index = models.IntegerField(null=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='player_deck')
    in_deck = models.BooleanField(default=True)

    class Meta:
        ordering = ['-index']

class Player(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hand = models.ManyToManyField(DeckCard)


class Game(models.Model):
    CHOICES = [
        ('S', 'Starting'),
        ('I', 'In Progress'),
        ('L', 'Lost'),
        ('W', 'Won'),
    ]
    players = models.ManyToManyField(Player)
    outbreaks = models.IntegerField(default=0)
    infection_rate = models.IntegerField(default=2)
    status = models.CharField(default='S', max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cured = models.ManyToManyField(Disease)
    eradicated = models.ManyToManyField(Disease)


class ResearchStation(models.Model):
    location = models.ForeignKey('game.CityNode', on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_deployed = models.BooleanField(default=False)


class CityNode(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    cubes = models.ManyToManyField('Cube')

class Cube(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)


class Character(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


class Pawn(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    location = models.ForeignKey(CityNode, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)





