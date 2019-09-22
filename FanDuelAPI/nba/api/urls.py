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


urlpatterns = [
    path('', include(router.urls)),

    path('teams/<int:pk>/', 
         nv.TeamDetailViewSet.as_view(),
         name='team-detail'),

     path('players/<int:pk>/', 
         nv.PlayerDetailViewSet.as_view(),
         name='player-detail'),

    path('players/<int:player_id>/stats/', 
         nv.PlayerStatisticDetailViewSet.as_view(),
         name='player-stats-detail'),
    
    path('games/<int:game_id>/',
         nv.GameSpecificDetailViewSet.as_view(),
         name='game-gamestate-detail')

    
]

'''
path('games/', 
         nv.GamelViewSet.as_view(),
         name='games-list'),
 path('games/<int:pk>/', 
         nv.GameStateDetailViewSet.as_view(),
         name='gamestate-detail')
'''