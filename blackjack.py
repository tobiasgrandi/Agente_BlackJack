import numpy as np

class Player():
    def __init__(self):
        self.cards = []
        self.has_ace = False #Indica si hay un As en la mano

    def take_card(self, card):
        self.cards.append(card)
        self.has_ace = card == 1

class Dealer():
    def __init__(self):
        self.cards = []

    def take_card(self, card):
        self.cards.append(11 if card == 1 else card)

class BlackJack():
    def __init__(self):
        self.deck = [1,2,3,4,5,6,7,8,9,10,10,10]*4
        np.random.shuffle(self.deck) #Mezclar cartas
        self.player = Player()
        self.dealer = Dealer()
        self.deal_card() #Repartir cartas
        self.deal_card()
        self.take_card() #Repartir una carta al dealer

    def deal_cards(self):
        self.player.take_card(self.deck.pop)

    def take_card(self):
        self.dealer.cards.append(self.deck.pop)