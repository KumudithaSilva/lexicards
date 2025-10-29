from tkinter import Tk

from lexicards.core.singleton_meta import SingletonMeta
from lexicards.interfaces.i_ui import IUI
from tkinter import Canvas, Button


class LexiUi(IUI, metaclass=SingletonMeta):

    BACKGROUND_COLOR = "#B1DDC6"
    LABEL_TOP_FONT = ("Arial", 40, "italic")
    LABEL_BOTTOM_FONT = ("Arial", 60, "italic")


    def __init__(self, root: Tk, images: dict = None):
        if hasattr(self, "_initialized"):
            return

        self._root = root
        self._images = images or {}
        self._canvas = None
        self._known_button = None
        self._unknown_button = None
        self._initialized = True


    def set_title(self, title: str):
        pass

    def set_word(self, word: str):
        pass

    def get_title_text(self) -> str:
        pass

    def get_word_text(self) -> str:
        pass

    def set_known_callback(self, callback):
        pass

    def set_unknown_callback(self, callback):
        pass


    # -----------------------------
    # Mac-only optional methods
    # -----------------------------
    def add_audio_buttons(self):
        pass

    def add_status_bar(self):
        pass
