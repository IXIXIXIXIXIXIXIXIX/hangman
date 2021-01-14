class Player:

    def __init__(self):
        
        # State 0 is completely unhanged and state 6 is dead
        self.state = 0

    def guess_letter(self, game, letter):
        pass

    def guess_word(self, game, word):
        pass

    def is_dead(self):
        
        if self.state >= 6:
            return True
        else:
            return False

    def display_status():
        # TODO: make this print an ASCII representation of the state
        print(f"Status is currently {self.state}")
