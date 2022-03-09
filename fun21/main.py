import deal

class Fun21:

    def __init__(self):
        pass

if __name__ == '__main__':
    print("Welcome to Fun 21!")
    print("How many decks do you want to play?")
    d = input()

    deck = deal.Deck(int(d))
    #deck.show(deck.cards)
    deck.shuffle()
    deck.deal()



