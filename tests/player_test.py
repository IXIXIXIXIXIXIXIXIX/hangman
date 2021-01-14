import unittest
from src.player import Player
from src.game import Game


class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player = Player()
        self.game = Game("primary")

    def test_state_is_zero(self):
        self.assertEqual(0, self.player.state)

    def test_guess_letter(self):
        self.player.guess_letter(self.game, 'r')
        self.assertEqual(0, self.player.state)
    
    def test_guess_letter_wrong(self):
        self.player.guess_letter(self.game, 'g')
        self.assertEqual(1, self.player.state)

    def test_guess_word(self):
        self.player.guess_word(self.game, "primary")
        self.assertEqual(0, self.player.state)

    def test_guess_word_wrong(self):
        self.player.guess_word(self.game, "secondary")
        self.assertEqual(1, self.player.state)

    def test_is_dead_when_is_not(self):
        self.assertEqual(False, self.player.is_dead())

    def test_is_dead_when_dead(self):

        for i in range(7):
            self.player.guess_letter(self.game, 'q')
        
        self.assertEqual(True, self.player.is_dead())

    def test_status_display(self):
        # Status 0
        print("\n")
        self.player.display_status()
        self.player.guess_letter(self.game, 'q')

        # Status 1
        self.player.display_status()
        self.player.guess_letter(self.game, 'q')
        
        # Status 2
        self.player.display_status()
        self.player.guess_letter(self.game, 'q')

        # Status 3
        self.player.display_status()
        self.player.guess_letter(self.game, 'q')

        # Status 4
        self.player.display_status()
        self.player.guess_letter(self.game, 'q')

        # Status 5
        self.player.display_status()
        self.player.guess_letter(self.game, 'q')

        # Status 6
        self.player.display_status()

        self.assertEqual(True, True)