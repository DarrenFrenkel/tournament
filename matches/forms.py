from django import forms
from django.forms import ModelForm
from .models import Match, Tournament, Player

class MatchForm(ModelForm):
	class Meta:
		model = Match
		fields = ['winner']

class TournamentForm(ModelForm):
	class Meta:
		model = Tournament
		fields = ['tournament_name', 'players', 'max_players']

	def clean(self):
		cleaned_data = super(TournamentForm, self).clean()
		players = cleaned_data['players'].count()
		max_player = cleaned_data['max_players']
		msg = "Please ensure that the total of players equals the max players' field"
		if players < max_player:
			raise forms.ValidationError(msg)

class PlayerForm(ModelForm):
	class Meta:
		model = Player
		fields = ['name']
