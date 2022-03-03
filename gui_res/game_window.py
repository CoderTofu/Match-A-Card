import time
from tkinter import *
import threading
import time
import random


def game_gui(window, count, deck):
    game_window = Toplevel(window)
    random.shuffle(deck)  # shuffles deck randomly

    checking = []

    def thread_wait(seconds):
        time.sleep(seconds)
        nonlocal checking
        for check in checking:
            check.config(text="")

        checking = []

    def show_and_hide(btn, card):
        nonlocal checking
        btn_text = btn.cget("text")
        if btn_text == "":
            card_text = card.stringify()
            btn.config(text=card_text)
            checking.append(btn)
            if len(checking) == 2:
                thread_wait(1)
        else:
            btn.config(text="")

    button_list = []
    for i in range(0, count):
        # card = deck[i].stringify()

        # First of the card pair
        card_button = Button(
            game_window,
            width=3,
            height=1
        )
        # Pass the button widget and the random card class so we can change text config
        card_button.config(command=lambda btn=card_button, j=i: show_and_hide(btn, deck[j]))

        # Second of the card pair
        card_button_pair = Button(
            game_window,
            width=3,
            height=1
        )
        # Pass the button widget and the random card class so we can change text config
        card_button_pair.config(command=lambda btn=card_button_pair, j=i: show_and_hide(btn, deck[j]))

        button_list.append(card_button)
        button_list.append(card_button_pair)

    random.shuffle(button_list)

    CARD_PER_COLUMN = 3
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
