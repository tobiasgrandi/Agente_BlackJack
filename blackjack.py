import numpy as np

class Player():
    def __init__(self):
        self.cards = []
        self.total_usable_aces = 0 #Cantidad de As usables en la mano
        self.has_ace = bool(self.total_usable_aces) #Indica si hay un As en la mano
        self.total = 0 #Suma de las cartas

    def take_card(self, card):
        self.cards.append(card)

        if card == 1:
            self.total_usable_aces += 1
            self.has_ace = True

        self.total = sum(self.cards)

        for ace in range(self.total_usable_aces):
            self.total += 10

        while self.has_ace and self.total > 21:
            self.total_usable_aces -= 1
            self.total -= 10
            self.has_ace = self.total_usable_aces > 0

class Dealer():
    def __init__(self):
        self.cards = []
        self.total = 0 #Suma de las cartas

    def take_card(self, card):
        self.cards.append(11 if card == 1 else card)
        self.sum = sum(self.cards)

class BlackJack():
    def __init__(self):
        self.done = False #Estado del juego
        self.player_state = 'Playing' #Estado del jugador (Under 21, Over 21, Lose, Win)

    def reset(self): #Comenzar un nuevo juego
        self.deck = [1,2,3,4,5,6,7,8,9,10,10,10]*4
        np.random.shuffle(self.deck) #Mezclar cartas
        self.player = Player()
        self.dealer = Dealer()
        self.deal_card() #Repartir cartas al jugador
        self.deal_card()
        self.take_card() #Repartir una carta al dealer
        self.done = False

    def deal_card(self):
        self.player.take_card(self.deck.pop())

    def take_card(self):
        self.dealer.take_card(self.deck.pop())

    def get_state(self):
        return {'player_total': self.player.total,
                'player_state': self.player_state,
                'dealer': self.dealer.cards[0],
                'has_ace': 1 if self.player.has_ace else 0,
                'dealer_total': self.dealer.total}

    def calculate_player_state(self): #Calcular estado del jugador una vez se plantó
        if self.player.total > 21:
            self.player_state = 'Lose'
        elif self.dealer.sum > 21:
            self.player_state = 'Win'
        elif self.dealer.sum >= self.player.total:
            self.player_state = 'Lose'
        else:
            self.player_state = 'Win'

    def step(self, action): #Pasar de un estado a otro, según acción del jugador

        if action == 0: #El jugador pide
            self.deal_card()
            if self.player.total > 21:
                self.calculate_player_state()
                self.done = True
        else:   #El jugador se planta
            while self.dealer.sum <= 16:
                self.take_card()
            self.done = True
            self.calculate_player_state()