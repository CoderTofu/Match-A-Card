from tkinter import *
from gui_res.game_window import game_gui
from gui_res.gui_frames.select_frame import card_selection


def gui(deck):
    window = Tk()
    window.geometry("400x160")
    window.resizable(0, 0)

    main_frame = Frame(window)
    main_frame.pack(padx=20, pady=20)

    instructions = Label(
        main_frame,
        text="How many cards do you want to match?",
        font=("consolas", 12)
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

    num_of_windows = 0

    def generate_game():
        sel_count = int(count_label.cget("text"))
        if num_of_windows > 3:
            return
        game_gui(window, sel_count, deck)

    # This button takes the value of count_label and generates a window with a number of cards based on the value
    generate = Button(
        main_frame,
        text="Generate",
        width=10,
        borderwidth=2,
        relief="groove",
        command=generate_game
    )
    generate.pack()

    # container for all controls to control card count

    window.mainloop()
