import random
from collections import Counter, namedtuple
from typing import List, Tuple

import constants

Card = namedtuple("Card", ["suit", "value"])

# Deck class currently doesn't put cards back in the deck, so you need to
# re-instantiate it every time you deal a hand.
class Deck:
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [
            Card(suit, value) for suit in Deck.suits for value in Deck.values
        ]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()


def build_value_arr(hand: List[Card]) -> List[bool]:
    """Return a index of booleans corresponding to card presence."""
    value_arr = [None] * 14

    for _, value in hand:
        indices = constants.VALUE_TO_ARR_MAP[value]
        for index in indices:
            value_arr[index] = True

    return value_arr


def determine_payout(hand: List[Card], initial_bet: int) -> Tuple[str, int]:
    """Return the hand result and payout amount."""
    value_arr = build_value_arr(hand)
    is_straight = any(
        [all(value_arr[i : i + 5]) for i in range(len(value_arr) - 4)]
    )
    num_suits_in_hand = len({card.suit for card in hand})
    num_values_in_hand = len({card.value for card in hand})
    most_of_a_kind = max(
        Counter([card.value for card in hand]).values()
    )

    hand_result = constants.LOSE

    if num_suits_in_hand == 1 and all(value_arr[-5:]):
        hand_result = constants.ROYAL_FLUSH

    elif num_suits_in_hand == 1 and is_straight:
        hand_result = constants.STRAIGHT_FLUSH

    elif num_values_in_hand == 2:
        if most_of_a_kind == 4:
            hand_result = constants.FOUR_OF_A_KIND
        else:
            hand_result = constants.FULL_HOUSE

    elif num_suits_in_hand == 1:
        hand_result = constants.FLUSH

    elif is_straight:
        hand_result = constants.STRAIGHT

    elif most_of_a_kind == 3:
        hand_result = constants.THREE_OF_A_KIND

    elif num_values_in_hand == 3 and most_of_a_kind == 2:
        hand_result = constants.TWO_PAIR

    elif any(value_arr[constants.JACK_INDEX :]):
        hand_result = constants.JACKS_OR_BETTER

    return (
        hand_result,
        constants.PAYOUTS[hand_result][constants.BET_AMOUNTS[initial_bet]],
    )


def main():
    deck = Deck()
    hand = [deck.deal_one() for _ in range(5)]

    test_hand = [
        Card("hearts", "A"),
        Card("hearts", "3"),
        Card("diamonds", "3"),
        Card("diamonds", "5"),
        Card("diamonds", "4"),
    ]

    determine_payout(test_hand, 1)


if __name__ == "__main__":
    main()
