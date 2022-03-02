from tkinter import *
from gui_res.gui_frames.select_frame import card_selection


def gui():
    window = Tk()
    window.geometry("360x160")
    window.resizable(0, 0)

    main_frame = Frame(
        window,

    )
    main_frame.pack(padx=20, pady=20)

    instructions = Label(
        main_frame,
        text="How many cards do you want to match?"
    )
    instructions.pack()

    count = 6  # default number of cards to play with

    # label that will represent the count
    count_label = Label(
        main_frame,
        text=str(count)
    )
    count_label.pack()

    card_selection_frame = card_selection(main_frame, count_label)
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
