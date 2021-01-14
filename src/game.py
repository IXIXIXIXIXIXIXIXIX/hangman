class Game:

    def __init__(self, solution):

        self.solution = solution.upper();

        self.display = ""

        for letter in self.solution:
            self.display += '_'

    def length(self):
        return len(self.solution)
    
    def try_letter(self, letter):

        letter_upper = letter.upper()
        index = 0
        new_display = list(self.display)
        success = False

        for letter in self.solution:

            if letter == letter_upper:
                new_display[index] = letter_upper
                success = True
            
            index += 1
        self.display = "".join(new_display) 
        return success

    def try_word(self, word):

        if word.upper() == self.solution:
            self.display = self.solution
            return True

        return False

    def won(self):
       return not '_' in self.display 

    def reset(self, new_word):

        self.solution = new_word.upper();

        self.display = ""

        for letter in self.solution:
            self.display += '_' 
