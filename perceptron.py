from numpy.random import rand


class Perceptron:

    def __init__(self, model, alpha):
        self.model = model
        self.alpha = alpha
        self.theta = 0
        self.vector = [rand() * 10 - 5 for i in range(self.model.dimensions)]

    # perceptron training method
    def delta(self, inputs):
        guess, val, d = self.classify(inputs)

        # if classified wrong
        if guess != inputs[-1]:
            self.vector = [self.vector[i] - (d - val) * self.alpha * inputs[i] for i in range(len(self.vector))]
            self.theta = self.theta - (d - val) * self.alpha * -1

        return self.vector, self.theta

    # perceptron testing method
    def test(self, inputs):
        guess, val, d = self.classify(inputs)
        if guess == inputs[-1]:
            self.model.add_guessed(guess)

        return self.vector, self.theta

    # classification of data based on vector
    def classify(self, inputs):
        y = 0

        for i in range(self.model.dimensions):
            y += inputs[i] * self.vector[i]

        if y < self.theta:
            guess = self.model.get_category_by_number(1).get_name()
            val = 1
        else:
            guess = self.model.get_category_by_number(0).get_name()
            val = 0

        if isinstance(inputs[-1], str):
            d = self.model.get_category_by_name(inputs[-1]).get_val()
            return guess, val, d
        else:
            return guess, val
