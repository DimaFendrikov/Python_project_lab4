from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    player1_dice1 = random.randint(1, 6)
    player1_dice2 = random.randint(1, 6)
    player2_dice1 = random.randint(1, 6)
    player2_dice2 = random.randint(1, 6)
    
    player1_total = player1_dice1 + player1_dice2
    player2_total = player2_dice1 + player2_dice2

    if player1_total > player2_total:
        winner = "Гравець 1 переміг!"
    elif player1_total < player2_total:
        winner = "Гравець 2 переміг!"
    else:
        winner = "Нічия!"

    return render_template('index.html',
        player1_dice1=f"static/photo/dice-{player1_dice1}.png",player1_dice2=f"static/photo/dice-{player1_dice2}.png",
        player2_dice1=f"static/photo/dice-{player2_dice1}.png",player2_dice2=f"static/photo/dice-{player2_dice2}.png",
        player1_total=player1_total,player2_total=player2_total,winner=winner)