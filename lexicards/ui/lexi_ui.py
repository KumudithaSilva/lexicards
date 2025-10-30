from tkinter import Canvas, Button, Tk

from lexicards.core.singleton_meta import SingletonMeta
from lexicards.interfaces.i_ui import IUI


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
        self._title_text_id = None
        self._word_text_id = None
        self._known_button = None
        self._unknown_button = None
        self._audio_buttons = None
        self._initialized = True


    def set_canvas(self, canvas: Canvas):
        self._canvas = canvas

    def set_title_text_id(self, text_id: int):
        self._title_text_id = text_id

    def set_word_text_id(self, text_id: int):
        self._word_text_id = text_id

    def set_known_button(self, button: Button):
        self._known_button = button

    def set_unknown_button(self, button: Button):
        self._unknown_button = button

    def set_audio_buttons(self, button: Button):
        self._audio_buttons = button



    def get_canvas(self) -> Canvas:
        return self._canvas

    def get_title_text_id(self) -> int:
        return self._title_text_id

    def get_word_text_id(self) -> int:
        return self._word_text_id

    def get_known_button(self) -> Button:
        return self._known_button

    def get_unknown_button(self) -> Button:
        return self._unknown_button

    def get_audio_buttons(self) -> Button:
        return self._audio_buttons



    def set_title(self, title: str):
        if self._canvas and self._title_text_id:
            self._canvas.itemconfig(self._title_text_id, text=title)

    def set_word(self, word: str):
        if self._canvas and self._word_text_id:
            self._canvas.itemconfig(self._word_text_id, text=word)

    def get_title_text(self) -> str:
        return self._canvas.itemcget(self._title_text_id, "text") if self._canvas else ""

    def get_word_text(self) -> str:
        return self._canvas.itemcget(self._word_text_id, "text") if self._canvas else ""

    def set_known_callback(self, callback):
        if self._known_button:
            self._known_button.config(command=callback)

    def set_unknown_callback(self, callback):
        if self._unknown_button:
            self._unknown_button.config(command=callback)


    # -----------------------------
    # Mac-only optional methods
    # -----------------------------
    def add_audio_buttons(self, callback):
        if self._audio_buttons:
            self._audio_buttons.config(command=callback)

    def add_status_bar(self):
        pass
