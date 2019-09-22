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

    #time_left_in_quarter = serializers.TimeField(format='%H:%M', input_formats='%H:%M')

    class Meta:
        model = GameState
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    # Serializer for Game objects
    #game_gs = GameStateSerializer(many=True, read_only=True)

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
    games = GameSerializer(many=True)
    game_states = GameStateSerializer(many=True)

