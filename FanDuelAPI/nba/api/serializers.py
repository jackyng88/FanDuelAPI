from rest_framework import serializers

from ..models import Team, Player, PlayerStatistic, Game, GameState



class TeamSerializer(serializers.ModelSerializer):
    # Serializer for Team objects

    class Meta:
        model = Team
        fields = '__all__'


class PlayerStatisticSerializer(serializers.ModelSerializer):
    # Serializer for player statistics object

    class Meta:
        model = PlayerStatistic
        fields = '__all__'

    
class GameStateSerializer(serializers.ModelSerializer):
    # Serializer for game state objects

    class Meta:
        model = GameState
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    # Serializer for Game objects

    class Meta:
        model = Game
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    # Serializer for Player objects
    playerstatistic = PlayerStatisticSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class GameDetailSerializer(serializers.Serializer):
    # Serializer for the listing of Game and GameState objects into a list
    games = GameSerializer(many=True)
    game_states = GameStateSerializer(many=True)

