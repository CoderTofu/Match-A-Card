from tkinter import *
import threading
import time
import random

from gui_res.gui_frames.card_frame import card_frame


def game_gui(window, count, deck):
    """
    Takes in the original window, count selected, and deck generated.
    Creates a new window with the 3 params
    """
    game_window = Toplevel(window)
    random.shuffle(deck)  # shuffles deck randomly

    button_list = []  # List that will hold all button widgets
    checking = []  # List that will hold up to the 2 most recent buttons player pressed

    times_checked = 0
    check_label = Label(game_window,
                        text=f"You checked {times_checked} times.",
                        font=("Arial Black", 20))
    check_label.pack(padx=20, pady=20)

    grid_frame = card_frame(game_window)  # Frame where all cards will be contained
    grid_frame.pack(padx=10, pady=10)

    def game_over():
        pass

    def judge_delay(wait, first, second):
        nonlocal times_checked
        # Sets a delay then either changes the text to a check mark
        # or clears it if the two do not match each other

        # Then after that checks if all boxes are checked, so it can do a function
        time.sleep(wait)
        try:
            times_checked += 1
            check_label.config(text=f"You checked {times_checked} times.")
            if first.cget("text") == second.cget("text"):
                first.config(text="✔", bg="green")
                second.config(text="✔", bg="green")
                game_over()
            else:
                first.config(text="")
                second.config(text="")
        except TclError:
            print("An error occurred...")

    def show_and_hide(btn, card):
        nonlocal checking
        btn_text = btn.cget("text")
        if btn_text == "":
            card_text = card.stringify()
            btn.config(text=card_text)
            checking.append(btn)
            if len(checking) == 2:
                thread = threading.Thread(target=judge_delay, args=(0.5, checking[0], checking[1]))
                thread.start()
                checking.clear()
        elif btn_text == "✔":
            print("You already matched!")
        else:
            print("Oops you can't do that!")

    # A loop that creates 2 cards per 1 count
    for i in range(0, count):
        # First of the card pair
        card_button = Button(grid_frame)
        # Pass the button widget itself and the random card class, so we can change text config
        card_button.config(command=lambda btn=card_button, j=i: show_and_hide(btn, deck[j]))

        # Second of the card pair
        card_button_pair = Button(grid_frame)

        # Pass the button widget itself and the random card class, so we can change text config
        card_button_pair.config(command=lambda btn=card_button_pair, j=i: show_and_hide(btn, deck[j]))

        button_list.append(card_button)
        button_list.append(card_button_pair)

    random.shuffle(button_list)
    CARD_PER_COLUMN = round(count/4) * 2
    cell_row_count = 0
    cell_column_count = 0

    for button in button_list:
        button.config(
            width=6,
            height=3,
            font=("arial", 15)
        )
        if cell_row_count == CARD_PER_COLUMN:
            # if number of cell rows reach 3, reset number of cell row and create a new column
            cell_row_count = 0
            cell_column_count += 1
        button.grid(row=cell_row_count, column=cell_column_count)
        # Otherwise, just create a new row for the card
        cell_row_count += 1

    grid_frame.pack()
