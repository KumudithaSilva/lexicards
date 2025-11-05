from tkinter import Button, Canvas, Label

from lexicards.interfaces.ui.i_ui_base import IUiBase


class DesktopLexiUI(IUiBase):
    """Builder class for assembling Desktop UI."""

    BACKGROUND_COLOR = "#B1DDC6"
    LABEL_TOP_FONT = ("Arial", 40, "italic")
    LABEL_BOTTOM_FONT = ("Arial", 60, "italic")

    def __init__(self, root):
        self._root = root
        self._canvas = None
        self._title_label = None
        self._word_label = None
        self._known_button = None
        self._unknown_button = None

    def build_window(self):
        """Configure main window."""
        self._root.title("LexiCards Windows")
        self._root.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)
        self._root.resizable(False, False)
        return self._root

    def build_canvas(self, card_front_image):
        """Create and grid the canvas."""
        canvas = Canvas(self._root, width=800, height=526, highlightthickness=0)
        canvas.config(background=self.BACKGROUND_COLOR)
        canvas.create_image(400, 263, image=card_front_image)
        canvas.grid(row=0, column=0, columnspan=2)
        self._canvas = canvas
        return canvas

    def create_title_label(self):
        """Create a label for the language title."""
        self._title_label = Label(
            self._root, text="", font=self.LABEL_TOP_FONT, bg="white"
        )
        self._title_label.place(x=400, y=150, anchor="center")

    def create_word_label(self):
        """Create the main word display label."""
        self._word_label = Label(
            self._root, text="", font=self.LABEL_TOP_FONT, bg="white"
        )
        self._word_label.place(x=400, y=263, anchor="center")

    def build_buttons(self, wrong_image, right_image):
        """Create Known and Unknown buttons."""

        self._unknown_button = Button(
            image=wrong_image,
            highlightthickness=0,
            relief="flat",
            bg=self.BACKGROUND_COLOR
        )
        self._unknown_button.grid(row=1, column=0)

        self._known_button = Button(
            image=right_image,
            highlightthickness=0,
            relief="flat",
            bg=self.BACKGROUND_COLOR,
        )
        self._known_button.grid(row=1, column=1)
        return self._unknown_button, self._known_button

    # -- Interface Methods --
    def set_title(self, title: str):
        self._title_label.config(text=title)

    def set_word(self, word: str):
        self._word_label.config(text=word)

    def set_known_callback(self, callback):
        self._known_button.config(command=callback)

    def set_unknown_callback(self, callback):
        self._unknown_button.config(command=callback)

    def get_title_text(self) -> str:
        return self._title_label

    def get_word_text(self) -> str:
        return self._word_label

    def get_root(self):
        return self._root
