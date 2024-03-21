import os
from game import Game

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    score1 = game.get_player_score()
    score2 = game.get_delear_score()
    return render_template('blackjack.html', score1=score1, score2=score2, game=game)

@app.route("/add", methods=['GET', 'POST'])
def add():
    game.get_card_palyer()
    return redirect('/')

@app.route("/pass", methods=['GET', 'POST'])
def pas():
    game.set_player_pass()
    return redirect('/')

@app.route("/unpass", methods=['GET', 'POST'])
def unpas():
    game.set_player_unpass()
    return redirect('/')

@app.route("/finish", methods=['GET', 'POST'])
def finish():
    game.finish_round()
    return redirect('/')

@app.route("/start", methods=['GET', 'POST'])
def start():
    game.start_round()
    return redirect('/')


if __name__ == '__main__':
    game = Game()
    game.issue()
    # port = int(os.environ.get("PORT", 1234))
    app.run(host='0.0.0.0', port=1515)