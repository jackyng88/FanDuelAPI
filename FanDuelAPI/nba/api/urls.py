from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views as nv


router = DefaultRouter()
router.register(r'teams', nv.TeamViewSet)
router.register(r'players', nv.PlayerViewSet)
router.register(r'gamedates', nv.GameViewSet)
router.register(r'playerstats', nv.PlayerStatisticViewSet)
router.register(r'gamestates', nv.GameStateViewSet)
router.register(r'games', nv.GameDetailViewSet, 'games_gs')
router.register(r'games/(?P<game_id>\d+)', nv.GameSpecificDetailViewSet, 'game_id_detail')
router.register(r'players/(?P<player_id>\d+)/stats', nv.PlayerStatisticDetailViewSet, 'player_id_stat_detail')


urlpatterns = [
    path('', include(router.urls)),

    path('teams/<int:pk>/', 
         nv.TeamDetailViewSet.as_view(),
         name='team-detail'),

     path('players/<int:pk>/', 
         nv.PlayerDetailViewSet.as_view(),
         name='player-detail'),

]
