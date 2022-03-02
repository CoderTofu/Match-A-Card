from tkinter import *
from gui_res.gui_frames.select_frame import card_selection


def gui():
    window = Tk()
    window.geometry("720x480")

    instructions = Label(
        window,
        text="How many cards do you want to match?"
    )
    instructions.pack()

    count = 6  # default number of cards to play with

    # label that will represent the count
    count_label = Label(
        window,
        text=str(count)
    )
    count_label.pack()

    card_selection_frame = card_selection(window, count_label)
    card_selection_frame.pack()

    windows = []

    def generate_game():
        if len(windows) > 3:
            return
        new_window = Toplevel(window)
        temp_var = Label(
            new_window,
            text=count_label.cget("text")
        )
        windows.append(new_window)
        temp_var.pack()

    # This button takes the value of count_label and generates a window with a number of cards based on the value
    generate = Button(
        window,
        text="Generate",
        width=10,
        borderwidth=2,
        relief="groove",
        command=generate_game
    )
    generate.pack()

    # container for all controls to control card count

    window.mainloop()
