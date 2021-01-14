import unittest
from src.game import Game 


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("primary")
        self.game2 = Game("PRIMARY")

    def test_solution_length(self):
        self.assertEqual(7, self.game.length())

    def test_display(self):
        self.assertEqual("_______", self.game.display)

    def test_wrong_letter(self):
        result = self.game.try_letter('b')
        self.assertEqual(False, result)
        self.assertEqual("_______", self.game.display)

    def test_correct__letter(self):
        result = self.game.try_letter('i')
        self.assertEqual(True, result)
        self.assertEqual("__I____", self.game.display)

    def test_upper_letter(self):
        result = self.game.try_letter('I')
        self.assertEqual(True, result)
        self.assertEqual("__I____", self.game.display)

    def test_multi_letter(self):
        result = self.game.try_letter('r')
        self.assertEqual(True, result)
        self.assertEqual("_R___R_", self.game.display)

    def test_first_letter(self):
        result = self.game.try_letter('p')
        self.assertEqual(True, result)
        self.assertEqual("P______", self.game.display)

    def test_last_letter(self):
        result = self.game.try_letter('y')
        self.assertEqual(True, result)
        self.assertEqual("______Y", self.game.display)

    def test_not_won(self):
        self.assertEqual(False, self.game.won())

    def test_try_letter_all(self):

        for letter in "primary":
            result = self.game.try_letter(letter)
            self.assertEqual(True, result)

        self.assertEqual(True, self.game.won())
        self.assertEqual("PRIMARY", self.game.display)

    def test_try_word_wrong(self):
        result = self.game.try_word("secondary")
        self.assertEqual(False, result)
        self.assertEqual(False, self.game.won())
        self.assertEqual("_______", self.game.display)

    def test_try_word_correct(self):
        result = self.game.try_word("primary")
        self.assertEqual(True, result)
        self.assertEqual(True, self.game.won())
        self.assertEqual("PRIMARY", self.game.display)

    def test_try_word_correct_upper(self):
        result = self.game.try_word("PRIMARY")
        self.assertEqual(True, result)
        self.assertEqual(True, self.game.won())
        self.assertEqual("PRIMARY", self.game.display)

    def test_solution_length_upper_solution(self):
        self.assertEqual(7, self.game2.length())

    def test_display_upper_solution(self):
        self.assertEqual("_______", self.game2.display)

    def test_wrong_letter_upper_solution(self):
        result = self.game2.try_letter('b')
        self.assertEqual(False, result)
        self.assertEqual("_______", self.game2.display)

    def test_correct__letter_upper_solution(self):
        result = self.game2.try_letter('i')
        self.assertEqual(True, result)
        self.assertEqual("__I____", self.game2.display)

    def test_upper_letter_upper_solution(self):
        result = self.game2.try_letter('I')
        self.assertEqual(True, result)
        self.assertEqual("__I____", self.game2.display)

    def test_multi_letter_upper_solution(self):
        result = self.game2.try_letter('r')
        self.assertEqual(True, result)
        self.assertEqual("_R___R_", self.game2.display)

    def test_first_letter_upper_solution(self):
        result = self.game2.try_letter('p')
        self.assertEqual(True, result)
        self.assertEqual("P______", self.game2.display)

    def test_last_letter_upper_solution(self):
        result = self.game2.try_letter('y')
        self.assertEqual(True, result)
        self.assertEqual("______Y", self.game2.display)

    def test_not_won_upper_solution(self):
        self.assertEqual(False, self.game2.won())

    def test_try_letter_all_upper_solution(self):

        for letter in "primary":
            result = self.game2.try_letter(letter)
            self.assertEqual(True, result)

        self.assertEqual(True, self.game2.won())
        self.assertEqual("PRIMARY", self.game2.display)

    def test_try_word_wrong_upper_solution(self):
        result = self.game2.try_word("secondary")
        self.assertEqual(False, result)
        self.assertEqual(False, self.game2.won())
        self.assertEqual("_______", self.game2.display)

    
    def test_try_word_correct_upper_solution(self):
        result = self.game2.try_word("primary")
        self.assertEqual(True, result)
        self.assertEqual(True, self.game2.won())
        self.assertEqual("PRIMARY", self.game2.display)

    def test_try_word_correct_upper_upper_solution(self):
        result = self.game2.try_word("PRIMARY")
        self.assertEqual(True, result)
        self.assertEqual(True, self.game2.won())
        self.assertEqual("PRIMARY", self.game2.display)

    def test_tried_letters_empty(self):
        self.assertEqual(0, len(self.game.tried_letters))

    def test_tried_letters_populated(self):

        self.game.try_letter('q')
        self.game.try_letter('a')
        
        self.assertEqual(2, len(self.game.tried_letters))
        self.assertEqual('A', self.game.tried_letters[0])
        self.assertEqual('Q', self.game.tried_letters[1])

    def test_tried_letters_twice(self):

        self.game.try_letter('q')
        self.game.try_letter('q')
        
        self.assertEqual(1, len(self.game.tried_letters))

    def test_tried_words_empty(self):
        self.assertEqual(0, len(self.game.tried_letters))

    def test_tried_words_populated(self):

        self.game.try_word("xylophone")
        self.game.try_word("apple")
        
        self.assertEqual(2, len(self.game.tried_words))
        self.assertEqual("APPLE", self.game.tried_words[0])
        self.assertEqual("XYLOPHONE", self.game.tried_words[1])

    def test_tried_words_twice(self):

        self.game.try_word("xylophone")
        self.game.try_word("xylophone")
        
        self.assertEqual(1, len(self.game.tried_words))