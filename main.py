from classes.deck_class import Deck  # Class I made for this game

from gui_res.main_gui import gui  # GUI


def main():
    deck_class = Deck()  # initialize a deck
    deck = deck_class.generate()  # generate a deck

    gui(max_length=len(deck))  # initialize the gui
    
    
if __name__ == "__main__":
    main()
