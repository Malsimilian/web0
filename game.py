import random


class Deck:
    def __init__(self):
        self.cards = []
        for _ in range(4):
            for i in range(2, 10):
                self.cards.append(i)
            for j in range(4):
                self.cards.append(10)
            self.cards.append(11)
        self.cards.sort()


class Delear:
    def __init__(self):
        self.deck = Deck()

    def dealing(self):
        n = random.randint(0, len(self.deck.cards) - 1)
        return self.deck.cards.pop(n)

    def kill(self):
        return 'дилер убит. дилер больше не может добирать карты в этом раунде'

    def new_deck(self):
        if len(self.deck.cards) <= 30:
            self.deck = Deck()


class Game:
    def __init__(self):
        self.delear = Delear()
        self.delear_cards = []
        self.player_cards = []
        self.player_pass = False
        self.delear_pass = False
        self.player_win = False
        self.delear_win = False

    def get_card_palyer(self):
        self.player_cards.append(self.delear.dealing())

    def get_card_delear(self):
        self.delear_cards.append(self.delear.dealing())

    def issue(self):
        for i in range(2):
            self.get_card_palyer()
            self.get_card_delear()

    def summ_card(self, cards):
        summ = 0
        for card in cards:
            summ += card
        return summ

    def check_black_jack(self, cards):
        return self.summ_card(cards) == 21

    def check_player_win(self):
        if self.check_black_jack(self.player_cards):
            self.player_win = True
            return True
        if self.player_pass and self.delear_pass:
            if self.summ_card(self.player_cards) > self.summ_card(self.delear_cards):
                self.player_win = True
                return True
        return False

    def check_delear_win(self):
        if self.check_black_jack(self.delear_cards):
            return True
        if self.player_pass and self.delear_pass:
            if self.summ_card(self.player_cards) < self.summ_card(self.delear_cards):
                return True
        return False

    def check_win_loss(self):
        if self.player_loss():
            self.delear_win = True
        elif self.delear_loss():
            self.player_win = True
        elif self.push():
            self.delear_win = True
        elif self.check_delear_win():
            self.delear_win = True
        elif self.check_player_win():
            self.player_win = True

    def player_loss(self):
        return self.summ_card(self.player_cards) > 21

    def delear_loss(self):
        return self.summ_card(self.delear_cards) > 21

    def push(self):
        if self.check_black_jack(self.player_cards) and self.check_black_jack(self.delear_cards):
            return True
        if self.player_pass and self.delear_pass:
            if self.summ_card(self.player_cards) == self.summ_card(self.delear_cards):
                return True
        return False

    def player_tactick(self):
        rezult = input(f'{self.summ_card(self.player_cards)} Добираем?')
        if 'да' in rezult or 'Да' in rezult or 'ДА' in rezult:
            return True
        return False

    def delear_tactick(self):
        if self.summ_card(self.delear_cards) > 15:
            return False
        return True

    def the_game_itself(self):
        if not self.player_pass:
            if self.player_tactick():
                self.get_card_palyer()
            else:
                self.player_pass = True
        elif not self.delear_pass:
            if self.delear_tactick():
                self.get_card_delear()
            else:
                self.delear_pass = True

    def start_round(self):
        self.delear_cards = []
        self.player_cards = []
        self.player_pass = False
        self.delear_pass = False
        self.player_win = False
        self.delear_win = False
        self.delear.new_deck()
        self.issue()

    def finish_round(self):
        pass


    def set_player_pass(self):
        self.player_pass = True

    def set_player_unpass(self):
        self.player_pass = False

    def get_player_score(self):
        return self.summ_card(self.player_cards)

    def get_delear_score(self):
        return self.summ_card(self.delear_cards)

    def delear_play(self):
        while self.delear_tactick():
            self.get_card_delear()
        self.delear_pass = True

    def is_win(self):
        if self.player_win or self.delear_win:
            return True
        return False


if __name__ == '__main__':
    deck = Deck()
    print(21 - sum(deck.cards) / len(deck.cards))
