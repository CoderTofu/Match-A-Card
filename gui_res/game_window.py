from tkinter import *
import random


def game_gui(window, count, deck):
    game_window = Toplevel(window)
    random_indexes = []
    for i in range(0, count):
        while True:  # to make sure that no index would be repeated
            random_index = random.randint(0, len(deck))
            if random_index not in random_indexes:
                random_indexes.append(random_index)
                break

    for index in random_indexes:
        temp_var = Button(
            game_window,
            text=deck[index].stringify(),
            width=3,
            height=1
        )
        temp_var.pack(padx=10, pady=10)
