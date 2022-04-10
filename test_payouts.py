import unittest
from random import randint

import constants
from determine_payout import Card, determine_payout


class PayoutTest(unittest.TestCase):
    def test_royal_flush(self):
        hand = [
            Card("diamonds", "A"),
            Card("diamonds", "K"),
            Card("diamonds", "Q"),
            Card("diamonds", "J"),
            Card("diamonds", "10"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.ROYAL_FLUSH)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.ROYAL_FLUSH][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )

    def test_straight_flush(self):
        hand = [
            Card("diamonds", "9"),
            Card("diamonds", "K"),
            Card("diamonds", "Q"),
            Card("diamonds", "J"),
            Card("diamonds", "10"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.STRAIGHT_FLUSH)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.STRAIGHT_FLUSH][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )

    def test_four_of_a_kind(self):
        hand = [
            Card("hearts", "2"),
            Card("hearts", "2"),
            Card("diamonds", "2"),
            Card("diamonds", "2"),
            Card("diamonds", "10"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.FOUR_OF_A_KIND)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.FOUR_OF_A_KIND][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )

    def test_full_house(self):
        hand = [
            Card("hearts", "2"),
            Card("hearts", "2"),
            Card("diamonds", "2"),
            Card("diamonds", "3"),
            Card("diamonds", "3"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.FULL_HOUSE)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.FULL_HOUSE][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )

    def test_flush(self):
        hand = [
            Card("diamonds", "2"),
            Card("diamonds", "2"),
            Card("diamonds", "4"),
            Card("diamonds", "3"),
            Card("diamonds", "3"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.FLUSH)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.FLUSH][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )

    def test_straight(self):
        hand = [
            Card("clubs", "3"),
            Card("diamonds", "4"),
            Card("diamonds", "5"),
            Card("diamonds", "6"),
            Card("diamonds", "7"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.STRAIGHT)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.STRAIGHT][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )

    def test_three_of_a_kind(self):
        hand = [
            Card("clubs", "3"),
            Card("diamonds", "3"),
            Card("diamonds", "3"),
            Card("diamonds", "6"),
            Card("diamonds", "7"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.THREE_OF_A_KIND)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.THREE_OF_A_KIND][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )

    def test_two_pair(self):
        hand = [
            Card("clubs", "3"),
            Card("diamonds", "3"),
            Card("diamonds", "6"),
            Card("diamonds", "6"),
            Card("diamonds", "7"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.TWO_PAIR)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.TWO_PAIR][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )

    def test_jacks_or_better(self):
        hand = [
            Card("clubs", "J"),
            Card("diamonds", "3"),
            Card("diamonds", "6"),
            Card("diamonds", "6"),
            Card("diamonds", "7"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.JACKS_OR_BETTER)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.JACKS_OR_BETTER][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )

    def test_lose(self):
        hand = [
            Card("clubs", "9"),
            Card("diamonds", "3"),
            Card("diamonds", "6"),
            Card("diamonds", "6"),
            Card("diamonds", "7"),
        ]
        bet_amount = randint(1, 5)

        hand_result, winnings = determine_payout(hand, bet_amount)
        self.assertEqual(hand_result, constants.LOSE)
        self.assertEqual(
            winnings,
            constants.PAYOUTS[constants.LOSE][
                constants.BET_AMOUNTS[bet_amount]
            ],
        )


if __name__ == "__main__":
    unittest.main()
