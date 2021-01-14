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

    def display_status(self):
        # TODO: make this print an ASCII representation of the state

        if self.state == 0:
            pass
        elif self.state == 1:
            pass

        else:
            print("\n")
            print("____")
            print("|   |")
            print("|   O")
            print("|  /|\\ ")
            print("|   |")
            print("|  / \\")
            print("| /   \\")
            print("|_________")
        print(f"Status is currently {self.state}")
