class Game:

    def __init__(self, solution):

        self.solution = solution.upper();

        self.display = ""
        self.tried_letters = []
        self.tried_words = []

        for letter in self.solution:
            self.display += '_'

    def length(self):
        return len(self.solution)
    
    def try_letter(self, letter):

        letter_upper = letter.upper()
        if not letter_upper in self.tried_letters:
            self.tried_letters.append(letter_upper)
            self.tried_letters = sorted(self.tried_letters)

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

        word_upper = word.upper()

        if not word_upper in self.tried_words:
            self.tried_words.append(word_upper)
            self.tried_words = sorted(self.tried_words)

        if word_upper == self.solution:
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

        self.tried_letters =[]
        self.tried_words = []
