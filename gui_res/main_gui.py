from tkinter import *
from gui_res.gui_frames.select_frame import card_selection


def gui(max_length):
    window = Tk()
    window.geometry("720x480")

    instructions = Label(
        window,
        text="How many cards do you want to match?"
    )
    instructions.pack()

    card_selection_frame = card_selection(window, max_length)
    card_selection_frame.pack()

    # container for all controls to control card count

    window.mainloop()
