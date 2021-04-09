from matplotlib import pyplot as plt
from matplotlib import animation
import itertools as it
import numpy as np
from model import column


class Graphs:

    def __init__(self, view):
        self.view = view

    def show_graphs(self, inputs, dim, colors, perceptron, type):
        # create figure
        fig = plt.figure(figsize=(7, 7))

        # calculate combinations of axes
        columns = [i for i in range(dim)]
        combinations = list(it.combinations(columns, 3))

        # list of dit every plot in figure
        plots = []

        # create a 3d plot for every combination (without repetition) of data
        for i in range(len(combinations)):
            plots.append({})
            plots[i]["axes"] = combinations[i]

            column1 = column(inputs, combinations[i][0])
            column2 = column(inputs, combinations[i][1])
            column3 = column(inputs, combinations[i][2])

            ax = fig.add_subplot(int(dim / 2), int(dim / 2), i + 1, projection='3d')
            ax.set_zlim(min(column3), max(column3))

            ax.set_xlabel("Column " + str(combinations[i][0] + 1))
            ax.set_ylabel("Column " + str(combinations[i][1] + 1))
            ax.set_zlabel("Column " + str(combinations[i][2] + 1))

            plots[i]["ax"] = ax

            plots[i]["scatter"] = ax.scatter(column1, column2, column3, c=colors)

            X = np.linspace(min(column1), max(column1), 6)
            Y = np.linspace(min(column2), min(column2), 6)
            X, Y = np.meshgrid(X, Y)
            Z = np.ones(X.shape, float) * 3
            surface = [ax.plot_surface(X, Y, Z, alpha=1.0)]
            plots[i]["surface"] = surface

            train_scatter = ax.scatter(column1, column2, column3, c=colors, cmap="Paired", alpha=0.2)

            test_scatter, = ax.plot([], [], [], 'ro', markersize='4', alpha=1.0)
            plots[i]["test_scatter"] = test_scatter

        # create animation for created figure of plots
        anim = animation.FuncAnimation(fig, self.update_animation, len(inputs), fargs=(inputs, plots, perceptron, type),
                                       init_func=self.init, repeat=False)

        plt.show()

    # for every plot in figure, update its data with currently tested input
    def update_animation(self, num, inputs, plots, perceptron, type):

        # theta value
        global theta
        # perceptron vector
        global normal

        # process current data row in perceptron
        if type == "train":
            normal, theta = perceptron.delta(inputs[num])
        elif type == "test":
            normal, theta = perceptron.test(inputs[num])
            self.view.get_label("accuracy") \
                .config(text="Total accuracy level: " + "{:.4f}".format(
                (perceptron.model.get_category_by_number(0).get_guessed()
                 + perceptron.model.get_category_by_number(1).get_guessed())
                / len(inputs)) + " / 1.00")
            self.view.get_label("class1").config(
                text=perceptron.model.get_category_by_number(0).get_name() + " {:.4f}".format(
                    perceptron.model.get_category_by_number(
                        0).get_guessed() / perceptron.model.get_category_by_number(0).get_size()) + " / 1.00")
            self.view.get_label("class2").config(
                text=perceptron.model.get_category_by_number(1).get_name() + " {:.4f}".format(
                    perceptron.model.get_category_by_number(
                        1).get_guessed() / perceptron.model.get_category_by_number(1).get_size()) + " / 1.00")

        # plane from normal and point
        theta = -theta
        normal = np.array(normal)

        # update data of all plots
        for plot in plots:
            axes = plot["axes"]
            xx, yy = np.meshgrid(np.linspace(min(column(inputs, axes[0])), max(column(inputs, axes[0])), 6),
                                 np.linspace(min(column(inputs, axes[1])), max(column(inputs, axes[1])), 6))
            z = (-normal[axes[0]] * xx - normal[axes[1]] * yy - theta) * 1. / normal[axes[2]]

            plot["test_scatter"].set_data(np.asarray(inputs[num][axes[0]]), np.asarray(inputs[num][axes[1]]))
            plot["test_scatter"].set_3d_properties(inputs[num][axes[2]])

            plot["surface"][0].remove()
            plot["surface"][0] = plot["ax"].plot_surface(xx, yy, z, alpha=0.7)

    # custom animation init function
    def init(self):
        pass
