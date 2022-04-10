from typing import List
from collections import namedtuple

import random

# initial_bet = [1, 2, 3, 4, 5]
# payout = {
#     "Royal Flush": [250, 500, 750, 1000, 4000],
#     "Straight Flush": [50, 100, 150, 200, 250],
#     "Four of a Kind": [25, 50, 75, 100, 125],
#     "Full House": [9, 18, 27, 36, 45],
#     "Flush": [6, 12, 18, 24, 30],
#     "Straight": [4, 8, 12, 16, 20],
#     "Three of a Kind": [3, 6, 9, 12, 15],
#     "Two Pair": [2, 4, 6, 8, 10],
#     "Jacks or Better": [1, 2, 3, 4, 5],
# }

Card = namedtuple('Card', 'suit value')


# Deck class currently doesn't put cards back in the deck, so you need to re-instantiate it every time you deal a hand.
class Deck:
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()


def determine_payout(hand: List['Card'], initial_bet: int) -> (str, int):
    print(hand)
    return "Three of a Kind", 25


def main():
    deck = Deck()
    hand = [deck.deal_one() for _ in range(5)]
    determine_payout(hand, 1)

    test_hand = [
        Card('diamond', '2'),
        Card('diamond', '3'),
        Card('diamond', '4'),
        Card('diamond', '5'),
        Card('diamond', '6')
    ]

    # You can write simple asserts to test your code
    assert (determine_payout(test_hand, 5) == ('Straight Flush', 250))


if __name__ == '__main__':
    main()
