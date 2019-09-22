from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Team(models.Model):
    # class for Team model

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    full_name = models.CharField(max_length=255)
    abbrev = models.CharField(max_length=10)


class Player(models.Model):
    # class for Player model

    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Game(models.Model):
    # class for Game model

    home_team = models.ForeignKey(Team, related_name='home_games',
                                     on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games',
                                     on_delete=models.CASCADE)
    date = models.DateField()


class PlayerStatistic(models.Model):
    # class for individual player statistics

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    assists = models.IntegerField()
    rebounds = models.IntegerField()
    nerd = models.FloatField()


class GameState(models.Model):
    # class for state of the game

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()
    broadcast = models.TextField(max_length=50)
    # quarter is a field that has to be at least 1 and at most 4, thus using
    # Django's validators.
    quarter = models.IntegerField(
                default=1,
                validators=[
                    MinValueValidator(1),
                    MaxValueValidator(4)
                ]
    )
    time_left_in_quarter = models.CharField(max_length=6)
    game_status = models.CharField(max_length=30)