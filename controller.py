import csv
from model import encode
from perceptron import Perceptron


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model

        # setting actions of view buttons
        view.set_command("read", self.read)
        view.set_command("train", self.train)
        view.set_command("test", self.test)
        view.set_command("classify", self.classify)

    # reading csv files
    def read(self):
        try:
            path = self.view.entries["trainpath"].get()
            with open(path) as f:
                reader = csv.reader(f, delimiter=';')
                self.model.set_trainset(list(reader))

                # Conversion of number type columns to float
                for train in self.model.trainset:
                    self.model.add_class(train[-1])
                    for i in range(len(train) - 1):
                        train[i] = float(train[i])

                # Set colors based on class name
                self.model.set_train_colors([encode(row[-1]) for row in self.model.trainset])
                
            path = self.view.entries["testpath"].get()
            with open(path) as f:
                reader = csv.reader(f, delimiter=';')
                self.model.set_testset(list(reader))

                # Conversion of number type columns to float
                for test in self.model.testset:
                    self.model.get_category_by_name(test[-1]).increase_size()
                    for i in range(len(test) - 1):
                        test[i] = float(test[i])

                # Set colors based on class name
                self.model.set_test_colors([encode(row[-1]) for row in self.model.testset])

            # Set dimensions of data in model 
            self.model.set_dimensions()
            # UI feedback
            self.view.get_entry("trainpath").config({"background": "pale green"})
            self.view.get_entry("testpath").config({"background": "pale green"})
            self.view.set_button_normal("train")
        except FileNotFoundError:
            # UI feedback
            self.view.get_entry("trainpath").config({"background": "tomato"})
            self.view.get_entry("testpath").config({"background": "tomato"})

    def train(self):
        alpha = float(self.view.get_entry("alpha").get())
        self.model.set_perceptron(Perceptron(self.model, alpha))
        self.view.set_button_normal("test")
        self.view.set_button_normal("classify")
        self.view.graphs.show_graphs(self.model.trainset, self.model.dimensions, self.model.train_colors,
                                     self.model.perceptron, "train")

    def test(self):
        self.model.reset_scores()
        self.view.graphs.show_graphs(self.model.testset, self.model.dimensions, self.model.test_colors,
                                     self.model.perceptron, "test")

    def classify(self):
        data = self.view.get_entry("data").get().split(';')
        data = [float(d) for d in data]
        guess,_ = self.model.perceptron.classify(data)
        self.view.get_label("guess").config(text="Classification result: " + guess)
