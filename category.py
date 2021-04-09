

class Category:

    val = 0

    def __init__(self, name):
        self.name = name
        self.val = Category.val
        self.size = 0
        self.guessed = 0
        Category.val += 1

    def increase_size(self):
        self.size += 1

    def increase_guessed(self):
        self.guessed += 1

    def get_name(self):
        return self.name

    def get_val(self):
        return self.val
    
    def get_size(self):
        return self.size

    def get_guessed(self):
        return self.guessed

    def reset_score(self):
        self.guessed = 0