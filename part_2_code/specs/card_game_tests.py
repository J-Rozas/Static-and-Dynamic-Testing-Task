import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        first_card = Card("hearts", 1)
        second_card = Card("diamonds", 3)
        third_card = Card("diamonds", 10)
        self.card_game = CardGame([first_card, second_card, third_card])

    def test_check_for_ace(self):
        card = self.card_game.cards[0]
        result = self.card_game.check_for_ace(card)
        self.assertEqual(True, result)

    def test_highest_card(self):
        first_card = self.card_game.cards[1]
        second_card = self.card_game.cards[2]
        highest_card = self.card_game.highest_card(first_card, second_card)
        self.assertEqual(second_card, highest_card)

    def test_cards_total(self):
        cards = self.card_game.cards
        total = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 14", total)