from category import Category


# returns specified column of given matrix
def column(matrix, i):
    return [row[i] for row in matrix]


# encoding string to int value
def encode(name):
    i = 0
    for c in name:
        i += ord(c)
    return i


class Model:

    def __init__(self, root):
        self.root = root
        self.perceptron = None
        self.trainset = None
        self.testset = None
        self.train_colors = None
        self.test_colors = None
        self.dimensions = 0
        self.categories = {}

    def set_perceptron(self, perceptron):
        self.perceptron = perceptron

    def set_trainset(self, trainset):
        self.trainset = trainset

    def set_testset(self, testset):
        self.testset = testset

    def set_train_colors(self, colors):
        self.train_colors = colors

    def set_test_colors(self, colors):
        self.test_colors = colors

    def set_dimensions(self):
        self.dimensions = len(self.trainset[0]) - 1

    def add_class(self, name):
        if name not in self.categories:
            self.categories[name] = Category(name)

    def add_guessed(self, name):
        self.categories[name].increase_guessed()

    def get_category_by_number(self, number):
        for key in self.categories:
            if self.categories.get(key).get_val() == number:
                return self.categories.get(key)

    def get_category_by_name(self, name):
        if name in self.categories:
            return self.categories[name]

    def reset_scores(self):
        for key in self.categories:
            self.categories[key].reset_score()
