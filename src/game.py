class Game:

    def __init__(self, solution):

        self.solution = solution.upper();

        self.display = ""

        for letter in self.solution:
            self.display += '_'