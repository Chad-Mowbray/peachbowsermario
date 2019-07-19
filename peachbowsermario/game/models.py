from django.db import models

class Player(models.Model):
    name = models.CharField(null=False, default='Player 1', max_length=200, unique=True)

    def __str__(self):
        return f'ID: {self.id} {self.name}'

class Game(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE, related_name='player')
    playerWon = models.BooleanField(null=False)
    
    def __str__(self):
        return f'ID: {self.id} Game results -> Win: {self.playerWon} {self.player.name}'

class Round(models.Model):
    gameId = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='games')
    winStatus = models.BooleanField(null=False)
    playerChoice = models.CharField(null=False, max_length=200)
    computerChoice = models.CharField(null=False, max_length=200)

    def __str__(self):
        return f'Round results -> Win: {self.winStatus} - Player choice {self.playerChoice} : Computer choice {self.computerChoice}'
