import unittest
from src.logo import *

class TestLogo(unittest.TestCase):

    def test_logo(self):

        print_logo()

        self.assertEqual(True, True)