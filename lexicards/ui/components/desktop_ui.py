from tkinter import Button, Canvas

from lexicards.interfaces.ui.components.i_ui_base import IUiBase


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
        self._next_button = None
        self._canvas_image = None

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
        self._canvas_image = canvas.create_image(400, 263, image=card_front_image)
        canvas.grid(row=0, column=0, columnspan=3)
        self._canvas = canvas
        return canvas

    def create_title_label(self):
        """Create a title text on the canvas."""
        self._title_label = self._canvas.create_text(
            400, 150, text="", font=self.LABEL_TOP_FONT, fill="black"
        )

    def create_word_label(self):
        """Create a word text on the canvas."""
        self._word_label = self._canvas.create_text(
            400, 263, text="", font=self.LABEL_TOP_FONT, fill="black"
        )

    def build_buttons(self, wrong_image, right_image, next_image):
        """Create Known and Unknown buttons."""

        self._unknown_button = Button(
            image=wrong_image,
            highlightthickness=0,
            relief="flat",
            bg=self.BACKGROUND_COLOR,
        )
        self._unknown_button.grid(row=1, column=0, pady=(10, 0))

        self._known_button = Button(
            image=right_image,
            highlightthickness=0,
            relief="flat",
            bg=self.BACKGROUND_COLOR,
        )
        self._known_button.grid(row=1, column=1, pady=(10, 0))

        self._next_button = Button(
            image=next_image,
            highlightthickness=0,
            relief="flat",
            bg=self.BACKGROUND_COLOR,
        )
        self._next_button.grid(row=1, column=2, pady=(10, 0))

        return self._unknown_button, self._known_button, self._next_button

    # -- Interface Methods --
    def set_title(self, title: str):
        self._canvas.itemconfig(self._title_label, text=title)

    def set_word(self, word: str):
        self._canvas.itemconfig(self._word_label, text=word)

    def set_known_callback(self, callback):
        self._known_button.config(command=callback)

    def set_unknown_callback(self, callback):
        self._unknown_button.config(command=callback)

    def set_next_callback(self, callback):
        self._next_button.config(command=callback)

    def set_canvas_image(self, image):
        self._canvas.itemconfig(self._canvas_image, image=image)

    def set_canvas_color(self, color: str):
        self._canvas.itemconfig(self._title_label, fill=color)
        self._canvas.itemconfig(self._word_label, fill=color)

    def get_title_text(self) -> str:
        return self._canvas.itemcget(self._title_label, "text")

    def get_word_text(self) -> str:
        return self._canvas.itemcget(self._word_label, "text")

    def get_root(self):
        return self._root
