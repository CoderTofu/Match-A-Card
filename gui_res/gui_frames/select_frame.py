from tkinter import *


# This file is for the frame that will pick out the number of cards to play with

def card_selection(window, count_label):
    count = 6

    minimum_count = 3   # the minimum number of cards a player can play with
    maximum_count = 12  # the maximum number

    def add_count():
        nonlocal count
        if maximum_count < count + 1:
            # if count is too high
            return
        count += 1
        count_label.config(
            text=str(count)
        )   # updates the label for count
        scale.set(count)

    def subtract_count():
        nonlocal count
        if minimum_count > count - 1:
            # if count is too low
            return
        count -= 1
        count_label.config(
            text=str(count)
        )
        scale.set(count)

    def scale_control(val):
        nonlocal count
        count = int(val)
        count_label.config(
            text=str(count)
        )

    # Frame that we would return to pack
    controls = Frame(window,
                     relief="groove"
                     )

    add_button = Button(
        controls,
        text="+",
        width=5,
        borderwidth=2,
        relief="groove",
        command=add_count
    )

    subtract_button = Button(
        controls,
        text="-",
        width=5,
        borderwidth=2,
        relief="groove",
        command=subtract_count
    )

    scale = Scale(
        controls,
        orient=HORIZONTAL,
        showvalue=False,
        length=200,
        command=scale_control,
        to=maximum_count,
        from_=minimum_count
    )
    scale.set(count)

    subtract_button.grid(row=1, column=0)
    scale.grid(row=1, column=1, columnspan=5)
    add_button.grid(row=1, column=6)

    return controls
