import unittest
from src.word_chooser import word_chooser

class TestWordChooser(unittest.TestCase):

    def setUp(self):
        self.test_word = ""

    def test_word_chosen(self):
        self.test_word = word_chooser()

        self.assertGreater(len(self.test_word), 0)
        self.assertNotEqual("", self.test_word)