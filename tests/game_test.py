import unittest
from src.game import *


class TestGame(unittest.TestCase):

    def SetUp(self):
        game = Game("primary")
        game2 = Game("PRIMARY")

    def test_solution_length(self):
        self.assertEqual(7, game.length())

    def test_display(self):
        self.assertEqual("_______", game.display)

    def test_wrong_letter(self):
        result = game.try_letter('b')
        self.assertEqual(False, result)
        self.assertEqual("_______", game.display)

    def test_correct__letter(self):
        result = game.try_letter('i')
        self.assertEqual(True, result)
        self.assertEqual("__I____", game.display)

    def test_upper_letter(self):
        result = game.try_letter('I')
        self.assertEqual(True, result)
        self.assertEqual("__I____", game.display)

    def test_multi_letter(self):
        result = game.try_letter('r')
        self.assertEqual(True, result)
        self.assertEqual("_R___R_", game.display)

    def test_first_letter(self):
        result = game.try_letter('p')
        self.assertEqual(True, result)
        self.assertEqual("P______", game.display)

    def test_last_letter(self):
        result = game.try_letter('y')
        self.assertEqual(True, result)
        self.assertEqual("______Y", game.display)

    def test_not_won(self):
        self.assertEqual(False, game.won())

    def test_try_letter_all(self):

        for letter in "primary":
            result = game.try_letter(letter)
            self.assertEqual(True, result)

        self.assertEqual(True, game.won())
        self.assertEqual("PRIMARY", game.display)

    def test_try_word_wrong(self):
        result = game.try_word("secondary")
        self.assertEqual(False, result)
        self.assertEqual(False, game.won())
        self.assertEqual("_______", game.display)

    
    def test_try_word_correct(self):
        result = game.try_word("primary")
        self.assertEqual(True, result)
        self.assertEqual(True, game.won())
        self.assertEqual("PRIMARY", game.display)

    def test_try_word_correct_upper(self):
        result = game.try_word("PRIMARY")
        self.assertEqual(True, result)
        self.assertEqual(True, game.won())
        self.assertEqual("PRIMARY", game.display)


    def test_solution_length_upper_solution(self):
        self.assertEqual(7, game2.length())

    def test_display_upper_solution(self):
        self.assertEqual("_______", game2.display)

    def test_wrong_letter_upper_solution(self):
        result = game2.try_letter('b')
        self.assertEqual(False, result)
        self.assertEqual("_______", game2.display)

    def test_correct__letter_upper_solution(self):
        result = game2.try_letter('i')
        self.assertEqual(True, result)
        self.assertEqual("__I____", game2.display)

    def test_upper_letter_upper_solution(self):
        result = game2.try_letter('I')
        self.assertEqual(True, result)
        self.assertEqual("__I____", game2.display)

    def test_multi_letter_upper_solution(self):
        result = game2.try_letter('r')
        self.assertEqual(True, result)
        self.assertEqual("_R___R_", game2.display)

    def test_first_letter_upper_solution(self):
        result = game2.try_letter('p')
        self.assertEqual(True, result)
        self.assertEqual("P______", game2.display)

    def test_last_letter_upper_solution(self):
        result = game2.try_letter('y')
        self.assertEqual(True, result)
        self.assertEqual("______Y", game2.display)

    def test_not_won_upper_solution(self):
        self.assertEqual(False, game2.won())

    def test_try_letter_all_upper_solution(self):

        for letter in "primary":
            result = game2.try_letter(letter)
            self.assertEqual(True, result)

        self.assertEqual(True, game2.won())
        self.assertEqual("PRIMARY", game2.display)

    def test_try_word_wrong_upper_solution(self):
        result = game2.try_word("secondary")
        self.assertEqual(False, result)
        self.assertEqual(False, game2.won())
        self.assertEqual("_______", game2.display)

    
    def test_try_word_correct_upper_solution(self):
        result = game2.try_word("primary")
        self.assertEqual(True, result)
        self.assertEqual(True, game2.won())
        self.assertEqual("PRIMARY", game2.display)

    def test_try_word_correct_upper_upper_solution(self):
        result = game2.try_word("PRIMARY")
        self.assertEqual(True, result)
        self.assertEqual(True, game2.won())
        self.assertEqual("PRIMARY", game2.display)

