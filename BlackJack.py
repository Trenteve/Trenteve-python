import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self): #called when print is invoked in a class
        return f"{self.rank['rank']} of {self.suit}."

class Deck:
    def __init__(self): #self refers to an instance of a class that we've developed
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [
                {'rank' : 'A' , 'value' : 11},
                {'rank' : '2' , 'value' : 2}, 
                {'rank' : '3' , 'value' : 3},
                {'rank' : '4' , 'value' : 4},
                {'rank' : '5' , 'value' : 5}, 
                {'rank' : '6' , 'value' : 6}, 
                {'rank' : '7' , 'value' : 7},
                {'rank' : '8' , 'value' : 8}, 
                {'rank' : '9' , 'value' : 9},
                {'rank' : '10' , 'value' : 10},
                {'rank' : 'J' , 'value' : 10},
                {'rank' : 'Q' , 'value' : 10},
                {'rank' : 'K' , 'value' : 10},
            ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, num):
        cards_dealt = []
        for x in range(num):
            if len(self.cards) > 0:
                cards_dealt.append(self.cards.pop())
        return cards_dealt 

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calc_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            if card.rank['rank'] == 'A':
                has_ace = True
            card_value = int(card.rank['value'])
            self.value += card_value
        if has_ace and self.value > 21:
            self.value -= 10

deck = Deck()
deck.shuffle()
hand = Hand()
hand.add_card(deck.deal(2))
print(hand.cards[0], hand.cards[1])