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

@app.route("/blackjack/<info>", methods=['GET', 'POST'])
def blackjack(info):
    if info == 'add':
        game.get_card_palyer()
    elif info == 'pass':
        game.set_player_pass()
    elif info == 'start':
        game.start_round()
    if game.player_pass:
        game.delear_play()
    game.check_win_loss()
    return render_template('blackjack.html', game=game)

@app.route("/ss", methods=['GET', 'POST'])
def ss():
    return render_template('ss.html')


if __name__ == '__main__':
    game = Game()
    game.issue()
    # port = int(os.environ.get("PORT", 1234))
    app.run(host='0.0.0.0', port=1515)