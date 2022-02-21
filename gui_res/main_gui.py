from tkinter import *

def GUI(max_length):
    minimum_count = 3 # the minimum number of cards a player can play with

    def add_count():
        nonlocal count, count_label
        if (max_length < count + 1): return
        count += 1
        count_label.config(
            text=str(count)
        )

    def subtract_count():
        nonlocal count, count_label
        if (minimum_count > count - 1): return
        count -= 1
        count_label.config(
            text=str(count)
        )

    window = Tk()
    window.geometry("480x480")

    instructions = Label(
        window,
        text="How many cards do you want to match?"
    )
    instructions.pack()

    controls = Label(window)

    count = round(max_length / 2)
    count_label = Label(
        window,
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

    instructions.pack()
    count_label.pack()
    controls.pack()
    subtract_button.pack(side=RIGHT)
    add_button.pack(side=LEFT)

    window.mainloop()
