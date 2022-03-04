from classes.deck_class import Deck  # Class I made for this game

from gui_res.main_gui import gui  # GUI


def main():
    deck_class = Deck()  # initialize a deck
    generated_deck = deck_class.generate()  # generate a deck

    gui(generated_deck)  # initialize the gui

    
if __name__ == "__main__":
    main()
