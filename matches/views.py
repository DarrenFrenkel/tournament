from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Tournament, Match, Player
from .forms import MatchForm, TournamentForm, PlayerForm


# Create your views here.
def home(request):
    '''
    return the latest tournament to the homepage
    '''
    tournament = Tournament.objects.latest()
    return render(request, 'tournament.html', {'tournament': tournament})


def winner(request, match_id):
    '''
    Allows you to choose a winner for matches
    '''
    match = Match.objects.get(pk=match_id)
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match.winner = form.cleaned_data['winner']
            match.save()
            return HttpResponseRedirect('/')
    else:
        form = MatchForm()
        form.fields['winner'].queryset = Player.objects.filter(Q(player_one=match) | Q(player_two=match))
    return render(request, 'winner.html', {'form': form, 'match': match})


def new_tournament(request):
    '''
    Allows you to create new tournaments and create new players to play in tournaments
    '''
    if request.method == 'POST':
        if 'tournament_name' in request.POST:
            player_form = PlayerForm()
            tournament_form = TournamentForm(request.POST)
            if tournament_form.is_valid():
                new_tournament = tournament_form.save()
                new_tournament.create_matches()
                return HttpResponseRedirect('/')
        else:
            player_form = PlayerForm(request.POST)
            tournament_form = TournamentForm()
            if player_form.is_valid():
                player_form.save()
                return HttpResponseRedirect('/new_tournament')
    else:
        tournament_form = TournamentForm()
        player_form = PlayerForm()
    return render(request, 'new_tournament.html', {'tournament_form': tournament_form, 'player_form': player_form})
