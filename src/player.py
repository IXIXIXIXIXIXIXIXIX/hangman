class Player:

    def __init__(self):
        
        # State 0 is completely unhanged and state 6 is dead
        self.state = 0

    def guess_letter(self, game, letter):

        if not self.is_dead():
            if not game.try_letter(letter):
                self.state += 1

    def guess_word(self, game, word):

        if not self.is_dead():
            if not game.try_word(word):
                self.state += 1

    def is_dead(self):
        
        if self.state >= 6:
            return True
        else:
            return False

    def reset(self):
        self.state = 0

    def display_status(self):
        # TODO: make this print an ASCII representation of the state

        if self.state == 0:
            print("\n")
            print("______")
            print("|    |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|__________")

        elif self.state == 1:
            print("\n")
            print("______")
            print("|    |")
            print("|    O")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|__________")

        elif self.state == 2:
            print("\n")
            print("______")
            print("|    |")
            print("|    O")
            print("|    | ")
            print("|    | ")
            print("|")
            print("|")
            print("|__________")

        elif self.state == 3:
            print("\n")
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|")
            print("|  | |")
            print("|")
            print("|")
            print("|__________")

        elif self.state == 4:
            print("\n")
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\ ")
            print("|  | | |")
            print("|")
            print("|")
            print("|__________")

        elif self.state == 5:
            print("\n")
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\ ")
            print("|  | | |")
            print("|   / ")
            print("|  /   ")
            print("|__________")

        else:
            print("\n")
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\ ")
            print("|  | | |")
            print("|   / \\")
            print("|  /   \\")
            print("|__________")

        print("\n")
