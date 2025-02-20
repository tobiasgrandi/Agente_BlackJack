import numpy as np
from q_learning import Qlearning

class Player():
    def __init__(self):
        self.cards = []
        self.has_ace = False #Indica si hay un As en la mano
        self.sum = 0 #Suma de las cartas
        self.qlearning = Qlearning()

    def take_card(self, card):
        self.cards.append(card)
        self.has_ace = card == 1
        self.sum = sum(self.card)

class Dealer():
    def __init__(self):
        self.cards = []
        self.sum = 0 #Suma de las cartas

    def take_card(self, card):
        self.cards.append(11 if card == 1 else card)
        self.sum = sum(self.card)

class BlackJack():
    def __init__(self):
        self.deck = [1,2,3,4,5,6,7,8,9,10,10,10]*4
        np.random.shuffle(self.deck) #Mezclar cartas
        self.done = False #Estado del juego
        self.player_state = '' #Estado del jugador (Under 21, Over 21, Lose, Win)

    def reset(self): #Comenzar un nuevo juego
        self.player = Player()
        self.dealer = Dealer()
        self.deal_card() #Repartir cartas al jugador
        self.deal_card()
        self.take_card() #Repartir una carta al dealer

    def deal_card(self):
        self.player.take_card(self.deck.pop)

    def take_card(self):
        self.dealer.cards.append(self.deck.pop)

    def get_state(self):
        return {'sum_player': self.player.sum,
                'player_state': self.player_state,
                'dealer': self.dealer.cards[0],
                'has_ace': 1 if self.player.has_ace else 0}

    def step(self, action): #Pasar de un estado a otro, según acción del jugador

        if action == 0: #El jugador pide VER QUE PASA CON EL AS
            self.deal_card()
            if self.player.sum > 21:
                self.done = True
                self.player_state = 'Over 21'
            else:
                self.player_state = 'Under 21'
        else:
            while self.dealer.sum <= 16:
                self.take_card()
            self.done = True

            if self.dealer.sum >= self.player.state:
                self.player_state = 'Lose'
            else:
                self.player_state = 'Win'
            