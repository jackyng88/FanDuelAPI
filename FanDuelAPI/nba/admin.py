from django.contrib import admin
from .models import Team, Player, Game, PlayerStatistic, GameState

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Game)

admin.site.register(PlayerStatistic)
admin.site.register(GameState)