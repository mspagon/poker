import enum
import getch
import os
import random

from collections import namedtuple

import layouts


class DeckError(Exception): pass


TERMINAL_X, TERMINAL_Y = os.get_terminal_size()

Card = namedtuple('Card', 'suit value')

# Bet
initial_bet = [1, 2, 3, 4, 5]
payoutx = {
    "Royal Flush": [250, 500, 750, 1000, 4000],
    "Straight Flush": [50, 100, 150, 200, 250],
    "Four of a Kind": [25, 50, 75, 100, 125],
    "Full House": [9, 18, 27, 36, 45],
    "Flush": [6, 12, 18, 24, 30],
    "Straight": [4, 8, 12, 16, 20],
    "Three of a Kind": [3, 6, 9, 12, 15],
    "Two Pair": [2, 4, 6, 8, 10],
    "Jacks or Better": [1, 2, 3, 4, 5],
}


# clears the terminal window
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


class Player:
    def __init__(self):
        self.coins = 500


class Deck:
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    symbols = {
        'hearts': '♥',
        'diamonds': '♦',
        'clubs': '♣',
        'spades': '♠',
    }

    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()


def get_title():
    title = [
        r",--.   ,--.,--.   ,--.                  ,------.        ,--.                  ",
        r" \  `.'  / `--' ,-|  | ,---.  ,---.     |  .--. ' ,---. |  |,-. ,---. ,--.--. ",
        r"  \     /  ,--.' .-. || .-. :| .-. |    |  '--' || .-. ||     /| .-. :|  .--' ",
        r"   \   /   |  |\ `-' |\   --.' '-' '    |  | --' ' '-' '|  \  \\   --.|  |    ",
        r"    `-'    `--' `---'  `----' `---'     `--'      `---' `--'`--'`----'`--'    ",
    ]

    fmt = '{:^' + str(TERMINAL_X) + '}'

    output = []
    for line in title:
        output.append(fmt.format(line))

    return ''.join(output)


def get_payout():
    payout = [
        r"╔══════════════════════════╦══════════════╦═══════════════╦═══════════════╦═══════════════╦═══════════════╗",
        r"║          Payout          ║    1 coin    ║    2 coins    ║    3 coins    ║    4 coins    ║    5 coins    ║",
        r"╠══════════════════════════╬══════════════╬═══════════════╬═══════════════╬═══════════════╬═══════════════╣",
        r"║Royal Flush         250:1 ║     250      ║      500      ║      750      ║     1000      ║     1250      ║",
        r"║Straight Flush       50:1 ║      50      ║      100      ║      150      ║      200      ║      250      ║",
        r"║Four of a Kind       25:1 ║      25      ║       50      ║       75      ║      100      ║      125      ║",
        r"║Full House            9:1 ║       9      ║       18      ║       27      ║       36      ║       45      ║",
        r"║Flush                 6:1 ║       6      ║       12      ║       18      ║       24      ║       30      ║",
        r"║Straight              4:1 ║       4      ║        8      ║       12      ║       16      ║       20      ║",
        r"║Three of a Kind       3:1 ║       3      ║        6      ║        9      ║       12      ║       15      ║",
        r"║Two Pair              2:1 ║       2      ║        4      ║        6      ║        8      ║       10      ║",
        r"║Jacks or Better       1:1 ║       1      ║        2      ║        3      ║        4      ║        5      ║",
        r"╚══════════════════════════╩══════════════╩═══════════════╩═══════════════╩═══════════════╩═══════════════╝",
    ]

    fmt = '{:^' + str(TERMINAL_X) + '}'

    output = []
    for line in payout:
        output.append(fmt.format(line))

    return ''.join(output)


def get_cards(hand):
    group = ['          '.join(bunch) for bunch in zip(*[layouts.cards[card] for card in hand])]

    fmt = '{:^' + str(TERMINAL_X) + '}'

    output = []
    for line in group:
        output.append(fmt.format(line))

    return ''.join(output)


def get_buttons(hold):
    group = ['      '.join(bunch) for bunch in zip(*[layouts.buttons[x] for x in hold])]

    fmt = '{:^' + str(TERMINAL_X) + '}'

    output = []
    for line in group:
        output.append(fmt.format(line))

    return ''.join(output)


def determine_payout(hand):
    pass


def main():
    # s = '╭' + '─'* (TERMINAL_X - 2) + '╮'
    # print(s)
    # for _ in range(10):
    #     s = '│' + ' ' * (TERMINAL_X - 2) + '│'
    #     print(s)
    #
    # s = '╰' + '─'* (TERMINAL_X - 2) + '╯'
    # print(s)

    deck = Deck()

    hand = [deck.deal_one() for _ in range(5)]

    hold = ['hold', 'hold', 'hold', 'hold', 'hold']

    s_title = get_title()
    s_payout = get_payout()
    s_cards = get_cards(hand)
    s_buttons = get_buttons(hold)

    clear()

    while True:
        s_buttons = get_buttons(hold)
        h = []
        for i in range(len(hold)):
            if hold[i] == 'draw':
                h.append(Card('null', 'null'))
            else:
                h.append(hand[i])
        s_cards = get_cards(h)

        print(s_title)
        print(s_payout)
        print(s_cards)
        print(s_buttons)

        key = getch.getch()

        if key == '1':
            hold[0] = 'hold' if hold[0] == 'draw' else 'draw'
        if key == '2':
            hold[1] = 'hold' if hold[1] == 'draw' else 'draw'
        if key == '3':
            hold[2] = 'hold' if hold[2] == 'draw' else 'draw'
        if key == '4':
            hold[3] = 'hold' if hold[3] == 'draw' else 'draw'
        if key == '5':
            hold[4] = 'hold' if hold[4] == 'draw' else 'draw'
        if key == '\x1b':
            print('You pressed Esc!')
            break

        if key == '\n':
            if all(x == 'hold' for x in hold):
                break

        clear()

    print('done!')


if __name__ == '__main__':
    main()
