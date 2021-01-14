def get_option():

    player_input = ""

    while not (player_input.lower() == 'y' or player_input.lower() == 'n'):
        player_input = input("Would you like to play again (Y/N)? ")
    
    return player_input

def get_guess():

    player_input = input("Type a single letter to guess at a letter or type more than one letter to guess at the whole word: ")

    while not player_input.isalpha():
        player_input = input("Please type only letters: ")

    return player_input