from rest_framework import serializers
from .models import *
from django.utils import timezone

class GameSerializer(serializers.HyperlinkedModelSerializer):

	game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),slug_field='name')

	class Meta:
		model = Game
		fields = ('url', 'game_category','name','release_date','played')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):

	game = serializers.SlugRelatedField(queryset=Game.objects.all(),slug_field='name')

	player = serializers.SlugRelatedField(queryset=Game.objects.all(),slug_field='name')

	def validate_game(self, game):
		if game==None:
			raise serializers.ValidationError("Não possui jogo válido")
		return game

	def validate_player(self, player):
		if player==None:
			raise serializers.ValidationError("Não possui jogador válido")
		return player

	def validate(self, data):
		if data['score_date'] < timezone.now() and data['score']>=0 and data['score'] != None:
			return data
		raise serializers.ValidationError("Score Inválido")

	class Meta:
		model = Score
		fields = ('url', 'pk', 'score', 'score_date', 'player', 'game',)


class PlayerSerializer(serializers.HyperlinkedModelSerializer):

	scores = ScoreSerializer(many=True, read_only=True)

	class Meta:
		model = Player
		fields = ('url','name','gender','scores')

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = GameCategory
		fields = ('url', 'pk', 'name', 'games')