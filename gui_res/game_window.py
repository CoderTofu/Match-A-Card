from tkinter import *
import threading
import time
import random


def game_gui(window, count, deck):
    game_window = Toplevel(window)
    random.shuffle(deck)  # shuffles deck randomly

    button_list = []  # List that will hold all button widgets
    checking = []  # List that will hold up to the 2 most recent buttons player pressed

    def judge_delay(wait, first, second):
        # Sets a delay then either changes the text to a check mark
        # or clears it if the two do not match each other

        # Then after that checks if all boxes are checked so it can do a function
        time.sleep(wait)
        try:
            if first.cget("text") == second.cget("text"):
                first.config(text="✔")
                second.config(text="✔")
            else:
                first.config(text="")
                second.config(text="")
        except:
            print("An error occurred...")

    def show_and_hide(btn, card):
        nonlocal checking
        btn_text = btn.cget("text")
        if btn_text == "":
            card_text = card.stringify()
            btn.config(text=card_text)
            checking.append(btn)
            if len(checking) == 2:
                thread = threading.Thread(target=judge_delay, args=(1, checking[0], checking[1]))
                thread.start()
                checking = []
        elif btn_text == "✔":
            print("You already matched!")
        else:
            btn.config(text="")

    # A loop that creates 2 cards per 1 count
    for i in range(0, count):
        # First of the card pair
        card_button = Button(
            game_window,
            width=3,
            height=1
        )
        # Pass the button widget itself and the random card class so we can change text config
        card_button.config(command=lambda btn=card_button, j=i: show_and_hide(btn, deck[j]))

        # Second of the card pair
        card_button_pair = Button(
            game_window,
            width=3,
            height=1
        )
        # Pass the button widget itself and the random card class so we can change text config
        card_button_pair.config(command=lambda btn=card_button_pair, j=i: show_and_hide(btn, deck[j]))

        button_list.append(card_button)
        button_list.append(card_button_pair)

    random.shuffle(button_list)
    CARD_PER_COLUMN = round(count/4) * 2
    cell_row_count = 0
    cell_column_count = 0
    for button in button_list:
        if cell_row_count == CARD_PER_COLUMN:
            # if number of cell rows reach 3, reset number of cell row and create a new column
            cell_row_count = 0
            cell_column_count += 1
        button.grid(row=cell_row_count, column=cell_column_count)
        # Otherwise, just create a new row for the card
        cell_row_count += 1
