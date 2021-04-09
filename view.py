from tkinter import *
from tkinter import ttk
from graphs import Graphs


class View:

    def __init__(self, master=None):
        self.master = master
        self.graphs = Graphs(self)
        self.figure = None
        self.canvas = None
        self.labels = {}
        self.entries = {}
        self.buttons = {}

        self.createview()

    # adding elements of UI to window
    def createview(self):
        self.master.title("Perceptron")
        self.master.geometry("355x800")

        self.create_label("Train set path:", row=0)
        self.create_label("Test set path:", row=1)
        self.create_label("Value of aplha:", row=4)
        self.create_label(row=6, columnspan=2, varname="accuracy")
        self.create_label(row=7, columnspan=2, varname="class1")
        self.create_label(row=8, columnspan=2, varname="class2")
        self.create_label("Classify data:", row=10)
        self.create_label(row=13, columnspan=2, varname="guess")

        self.create_entry(0, 1, "trainpath")
        self.create_entry(1, 1, "testpath")
        self.create_entry(4, 1, "alpha")
        self.create_entry(10, 1, "data")

        self.create_button("Load data", row=2, columnspan=2, varname="read")
        self.create_button("Train Perceptron", row=5, column=0, varname="train", state=DISABLED)
        self.create_button("Test accuracy", row=5, column=1, varname="test", state=DISABLED)
        self.create_button("Classify", row=12, columnspan=2, varname="classify", state=DISABLED)

        self.create_separator(3, 2)
        self.create_separator(9, 2)

    # Universal methods of simple UI elements creation:

    def create_label(self, text="", textvar=None, row=0, column=0, columnspan=1, pady=10, padx=20, varname=""):
        if varname == "":
            varname = text
        self.labels[varname] = Label(master=self.master, text=text, textvariable=textvar)
        self.labels[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_entry(self, row, column, varname, columnspan=1, pady=10, padx=20,):
        self.entries[varname] = Entry(self.master)
        self.entries[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_button(self, text, row=0, column=0, columnspan=1, varname="", state=NORMAL, pady=10, padx=20,):
        if varname == "":
            varname = text
        self.buttons[varname] = Button(self.master, text=text, state=state, pady=5)
        self.buttons[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=padx)

    def create_separator(self, row, columnspan, orient="horizontal", pady=10, padx=0,):
        ttk.Separator(self.master, orient=orient).grid(row=row, columnspan=columnspan, sticky="ew", pady=pady, padx=padx)

    def set_command(self, varname, command):
        self.buttons[varname]["command"] = command

    def set_button_normal(self, varname):
        self.get_button(varname)["state"] = NORMAL

    def get_label(self, varname):
        return self.labels[varname]

    def get_entry(self, varname):
        return self.entries[varname]

    def get_button(self, varname):
        return self.buttons[varname]
