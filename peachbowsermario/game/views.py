import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Game
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def receive(request):
    if request.method == "POST":
        data = json.loads(request.body)
        db_player = Player.objects.create(name=data['name'])
        db_game = Game.objects.create(player=db_player.id)
        print("{ 'playerId': " + str(db_player[id]) + ", 'gameId': " + str(db_game[id]) + "}")
    
    return HttpResponse("{ 'playerId': " + str(db_player[id]) + ", 'gameId': " + str(db_game[id]) + "}")

