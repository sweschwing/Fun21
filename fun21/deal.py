#Code from https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3
import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        if self.value == 11:
            print("{} of {}".format('Jack', self.suit))
        elif self.value == 12:
            print("{} of {}".format('Queen', self.suit))
        elif self.value == 13:
            print("{} of {}".format('King', self.suit))
        elif self.value == 1:
            print("{} of {}".format('Ace', self.suit))
        else:
            print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self, num=1):
        self.cards = []
        self.pcards = []
        self.dcards = []
        self.build(num)

    def build(self, num):
        for x in range (0,num):
            for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
                for val in range(1,14):
                    self.cards.append(Card(suit, val))

    def show(self, deck):
        for card in deck:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def score(self, cards):
        vals = []
        total = 0
        for card in cards:
            vals.append(card.value)
            if card.value == 1 and total < 11:
                val = 11
            elif card.value == 1 and total > 10:
                val = 1
            elif card.value > 10:
                val = 10
            else:
                val = card.value
            total += val

        if 1 in vals and total > 21:
            #the ace should have been counted as 1 because later card pushed it over
            total -= 10
        return total

    def deal(self):
        play = True
        while play:
            self.pcards.append(self.cards.pop(0))
            self.dcards.append(self.cards.pop(0))
            self.pcards.append(self.cards.pop(0))
            self.dcards.append(self.cards.pop(0))

            print("Player cards: ")
            self.show(self.pcards)
            dc = self.dcards.pop()
            print("Dealer Card: ")
            dc.show()
            self.dcards.append(dc)

            move = 'h'
            while move == 'h':
                print("Hit or stand? Enter h or s")
                move = input()
                if move == 'h':
                    self.pcards.append(self.cards.pop(0))
                    print("Player cards: ")
                    self.show(self.pcards)

            #dealer deals until 17+ or bust
            print("Dealer's turn")
            move = 'h'
            while move == 'h':
                self.show(self.dcards)
                score = self.score(self.dcards)
                #print("Score ", score)
                if score < 17:
                    move = 'h'
                    self.dcards.append(self.cards.pop(0))
                else:
                    move = 's'

            pscore = self.score(self.pcards)
            dscore = self.score(self.dcards)

            print("**************Final score Player {}, Dealer {}".format(pscore, dscore))
            print("Player's cards: ")
            self.show(self.pcards)
            print("Dealer's cards: ")
            self.show(self.dcards)

            p_bust = False
            d_bust = False
            if pscore > 21:
                p_bust = True
            if dscore > 21:
                d_bust = True

            if d_bust and p_bust:
                print("BOTH BUST")
            elif (dscore > pscore and not d_bust) or (p_bust and not d_bust):
                print("DEALER WINS")
                if dscore == 21 and len(self.dcards) == 2:
                    print("******BLACKJACK********")
            elif pscore > dscore and not p_bust or (d_bust and not p_bust):
                print("PLAYER WINS")
                if pscore == 21 and len(self.pcards) == 2:
                    print("******BLACKJACK********")
            elif dscore == pscore:
                print("DRAW")


            print("Want to play again? Enter yes or no.")
            response = input()
            if response == "yes":
                play = True
            else:
                play = False
            if play:
                self.pcards = []
                self.dcards = []
                if len(self.cards) < 60:
                    self.cards = []
                    print("Must create new decks. How many decks do you want to play?")
                    num = input()
                    self.build(int(num))
