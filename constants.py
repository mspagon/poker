JACK_INDEX = 10

# Value and corresponding index in `value_arr`
VALUE_TO_ARR_MAP = {
    "A": [0, 13],
    "2": [1],
    "3": [2],
    "4": [3],
    "5": [4],
    "6": [5],
    "7": [6],
    "8": [7],
    "9": [8],
    "10": [9],
    "J": [10],
    "Q": [11],
    "K": [12],
}

# Hand results
ROYAL_FLUSH = "Royal Flush"
STRAIGHT_FLUSH = "Straight Flush"
FOUR_OF_A_KIND = "Four of a Kind"
FULL_HOUSE = "Full House"
FLUSH = "Flush"
STRAIGHT = "Straight"
THREE_OF_A_KIND = "Three of a Kind"
TWO_PAIR = "Two Pair"
JACKS_OR_BETTER = "Jacks or Better"
LOSE = "Lose"

# Key: Bet amount
# Value: corresponding index in `PAYOUTS`
BET_AMOUNTS = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
}

PAYOUTS = {
    ROYAL_FLUSH: [250, 500, 750, 1000, 4000],
    STRAIGHT_FLUSH: [50, 100, 150, 200, 250],
    FOUR_OF_A_KIND: [25, 50, 75, 100, 125],
    FULL_HOUSE: [9, 18, 27, 36, 45],
    FLUSH: [6, 12, 18, 24, 30],
    STRAIGHT: [4, 8, 12, 16, 20],
    THREE_OF_A_KIND: [3, 6, 9, 12, 15],
    TWO_PAIR: [2, 4, 6, 8, 10],
    JACKS_OR_BETTER: [1, 2, 3, 4, 5],
    LOSE: [0, 0, 0, 0, 0],
}
