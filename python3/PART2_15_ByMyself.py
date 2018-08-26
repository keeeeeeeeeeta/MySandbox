from random import shuffle

class Game:

class Deck:

class Player:
    def __init__(self, name):
        self.name = name
        self.win_count = 0

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None,"2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        """ num and mark are int"""
        self.value = value
        self.suit = suit

    def __gt__(self):
        pass

    def __repr__(self):
        """
        Returns str like "2 of Queen"
        :param self.value: int
        :param self.suit: int
        """
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v





game = Game()
game.play_game()