import os
from game import Game

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if game.player_pass:
        game.delear_play()
    game.check_win_loss()
    return render_template('blackjack.html', game=game)

@app.route("/add", methods=['GET', 'POST'])
def add():
    game.get_card_palyer()
    return redirect('/')

@app.route("/pass", methods=['GET', 'POST'])
def pas():
    game.set_player_pass()
    return redirect('/')

@app.route("/info", methods=['GET', 'POST'])
def unpas():
    print(game.player_cards, game.delear_cards)
    print(game.player_win, game.delear_win)
    print(game.player_pass, game.delear_pass)
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