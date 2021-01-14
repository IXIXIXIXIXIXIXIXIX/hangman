import os
from src.game import Game
from src.player import Player
from src.word_chooser import *
from src.input import *

def main():

    game_word = word_chooser() 
    game = Game(game_word)
    player = Player()
    option = 'y'

    while option != 'n':

        while not player.is_dead() and not game.won():

            # Next line found at https://stackoverflow.com/questions/2084508/clear-terminal-in-python
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("HANGMAN\n")

            print("Tried words:")
            print(", ".join(game.tried_words))
            print("Tried Letters:")
            print(", ".join(game.tried_letters))
            player.display_status()
            print(f"{game.display}\n")
            
            guess = get_guess()
            if len(guess) == 1:
                player.guess_letter(game, guess)
            else:
                player.guess_word(game, guess)

        
        if player.is_dead():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("HANGMAN\n")
            print("Tried words:")
            print(", ".join(game.tried_words))
            print("Tried Letters:")
            print(", ".join(game.tried_letters))
            player.display_status()
            print("Game Over!")
            print(f"The word you were looking for was: {game.solution}")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("HANGMAN\n")
            print("Tried words:")
            print(", ".join(game.tried_words))
            print("Tried Letters:")
            print(", ".join(game.tried_letters))
            player.display_status()
            print(f"{game.display}\n")
            print("Congratulations! You Won!\n")
    
        option = get_option()
        player.reset()
        game.reset(word_chooser())


if __name__ == "__main__":
    main()