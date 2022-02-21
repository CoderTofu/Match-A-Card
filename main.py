from classes.deck_class import Deck
from tkinter import *

def main():
    # deck = Deck()
    # deck.generate()
    # for card in deck.deck:
    #     card.show()

    window = Tk()
    label = Label(window,
        text="How many cards do you want to match?"
    )
    label.pack()
    window.mainloop()
    

if __name__ == "__main__":
    main()