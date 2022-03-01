from tkinter import *


def card_selection(window, max_length):
    count = round(max_length / 4)  # default number of cards to play with

    minimum_count = 3   # the minimum number of cards a player can play with

    def add_count():
        nonlocal count, count_label
        if max_length < count + 1:
            # if count is too high
            return
        count += 1
        count_label.config(
            text=str(count)
        )

    def subtract_count():
        nonlocal count, count_label
        if minimum_count > count - 1:
            # if count is too low
            return
        count -= 1
        count_label.config(
            text=str(count)
        )

    # Frame that we would return to pack
    controls = Frame(window)

    # label that will represent the count
    count_label = Label(
        controls,
        text=str(count)
    )

    add_button = Button(
        controls,
        text="+",
        command=add_count
    )

    subtract_button = Button(
        controls,
        text="-",
        command=subtract_count
    )

    count_label.pack()
    add_button.pack(side=LEFT)
    # SCALE will be packed here between the two add and subtract
    subtract_button.pack(side=RIGHT)
    # Generate button added here to generate a new window to start the game.
    # Can only generate up to 3 windows

    return controls
