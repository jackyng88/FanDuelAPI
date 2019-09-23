from django.db.models import Q

from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from datetime import datetime
from collections import namedtuple

from .serializers import (GameSerializer, GameStateSerializer, 
                          GameDetailSerializer, PlayerSerializer,
                          PlayerStatisticSerializer, TeamSerializer)
from ..models import Game, GameState, Player, PlayerStatistic, Team


Game_GS = namedtuple('Game_GS', ('games', 'game_states'))




def params_to_date(date_raw):
    # Converts a string from parameters into a date object.
    # Date parameter will be a string in the format of 'MMDDYYYY'
    # Note - _ before function is python convention for a private function
    # date_raw = '01012016'
    date = datetime.strptime(date_raw, '%m%d%Y').date()
    return date  


class TeamViewSet(viewsets.ModelViewSet):
    # ViewSet to display Teams

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        # overriding the perform_create
        serializer.save()


class PlayerViewSet(viewsets.ModelViewSet):
    # ViewSet to display Players

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def perform_create(self, serializer):
        # overriding the perform_create
        serializer.save()

    def get_queryset(self):
        # overriding get_queryset function
        # date_raw will be a string from the date query parameter
        date_raw = self.request.query_params.get('date')
        queryset = self.queryset
        if date_raw:
            #date = self._params_to_date(date_raw)
            date = params_to_date(date_raw)
            # Filtering the original queryset object on related_names -
            # home_games and away_games in the Game model. We match the dates
            # from those related_names with the date query parameter which is a
            # datetime.date() object and then we filter the queryset again 
            # with player_id's that exist in the PlayerStatistic table.
            qs_date_filtered = queryset.filter(Q(team__home_games__date=date) | Q(team__away_games__date=date))
            player_ids = PlayerStatistic.objects.values_list('player_id', flat=True)
            qs_date_playerstat = qs_date_filtered.filter(id__in=player_ids)
            return qs_date_playerstat
            
        # If no query parameters were provided, return the original queryset.
        return queryset


class GameViewSet(viewsets.ModelViewSet):
    # ViewSet to display Games

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save()


class PlayerStatisticViewSet(viewsets.ModelViewSet):
    # ViewSet to display player statistics

    queryset = PlayerStatistic.objects.all()
    serializer_class = PlayerStatisticSerializer

    def perform_create(self, serializer):
        serializer.save()


class TeamDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    # View for displaying the statistics of a given player
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    # View for displaying the object of a given player (by pk)
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerStatisticDetailViewSet(viewsets.ModelViewSet):
    # View for displaying the statistics of a given player.
    # will search by lookup_field in url with associated player_id integer.
    # In urls.py we specify this i.e. players/<int:player_id>/stats/
    queryset = PlayerStatistic.objects.all()
    serializer_class = PlayerStatisticSerializer
    #lookup_field = 'player_id'

    def get_queryset(self):
        return self.queryset.filter(player_id=self.kwargs['player_id'])


class GameStateViewSet(viewsets.ModelViewSet):
    # ViewSet to display Games

    queryset = GameState.objects.all()
    serializer_class = GameStateSerializer

    def perform_create(self, serializer):
        serializer.save()


class GameDetailViewSet(viewsets.ViewSet):
    # ViewSet for displaying game and gamestate as a list

    def list(self, request):
        date_raw = self.request.query_params.get('date')

        # if date_raw exists then we first filter the Game table's date field
        # by the date url parameter. Then game_ids gets the values of the
        # 'id' or the primary key field of Game. gs_filtered then gets 
        # filtered by matching if GameState's game_id field matches any of the
        # values from game_ids. At the end we return a named tuple of Game_GS
        # that looks in the form of something like {games: [], game_states:[]}
        if date_raw:
            date = params_to_date(date_raw)
            game_date_filtered = Game.objects.all().filter(date=date)
            game_ids = game_date_filtered.values_list('id', flat=True)
            gs_filtered = GameState.objects.all().filter(game_id__in=game_ids)

            game_gs = Game_GS(games=game_date_filtered,
                              game_states=gs_filtered)
            serializer = GameDetailSerializer(game_gs)
            return Response(serializer.data)

        game_gs = Game_GS(games=Game.objects.all(),
                          game_states=GameState.objects.all())
        serializer = GameDetailSerializer(game_gs)
        return Response(serializer.data)


class GameSpecificDetailViewSet(viewsets.ViewSet):
    # ViewSet for displaying specific Game and GameState by url game_id param

    def list(self, request, game_id):
        # Filters Game by the game_id as well as GameState. Returns a response
        # in the form of {games:[ {...} ], game_states:[ {...} ] }
        game_id = self.kwargs['game_id']
        games_filtered = Game.objects.all().filter(id=game_id)
        gs_filtered = GameState.objects.all().filter(game_id=game_id)
        game_gs = Game_GS(games=games_filtered,
                          game_states=gs_filtered)
        serializer = GameDetailSerializer(game_gs)

        return Response(serializer.data)