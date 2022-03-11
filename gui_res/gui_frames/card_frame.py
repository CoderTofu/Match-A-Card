from tkinter import *


def card_frame(game_window):
    """
    :param game_window: window where it will be packed in
    :return: a frame for tkinter
    """

    frame = Frame(game_window,
                  borderwidth=5,
                  relief="groove")

    return frame
