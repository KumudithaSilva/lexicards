from tkinter import Tk, Canvas, Button
from lexicards.ui.builders.base_builder import LexiUiBuilderAbstract
from lexicards.ui.lexi_ui import LexiUi


class DesktopLexiUiBuilder(LexiUiBuilderAbstract):

    def __init__(self, root: Tk, images=None, known_callback=None, unknown_callback=None):
        super().__init__(root, images)
        self._known_callback = known_callback
        self._unknown_callback = unknown_callback

    def create_new_ui(self):
        """Create singleton LexiUi instance."""
        self._ui = LexiUi(root=self._root, images=self._images)

    def build_window(self):
        """Configure main window."""
        self._root.title("LexiCards Windows")
        self._root.config(padx=50, pady=50, bg=LexiUi.BACKGROUND_COLOR)
        self._root.resizable(False, False)

    def build_canvas(self):
        """Create and grid the canvas."""
        canvas = Canvas(self._root, width=800, height=526, highlightthickness=0)
        canvas.config(background=LexiUi.BACKGROUND_COLOR)
        canvas.create_image(400, 263, image=self._images["card_front_image"])
        canvas.grid(row=0, column=0, columnspan=2)
        self._ui.set_canvas(canvas)
        return canvas

    def build_text_elements(self):
        """Create title and word text IDs."""
        title_id = self._ui.get_canvas().create_text(
            400, 150, text="Title", font=LexiUi.LABEL_TOP_FONT
        )
        word_id = self._ui.get_canvas().create_text(
            400, 263, text="Word", font=LexiUi.LABEL_BOTTOM_FONT
        )
        self._ui.set_title_text_id(title_id)
        self._ui.set_word_text_id(word_id)
        return title_id, word_id


    def build_buttons(self):
        # Button configuration
        unknown_button = Button(
            image=self._images["wrong_image"],
            highlightthickness=0,
            relief="flat",
            bg=LexiUi.BACKGROUND_COLOR,
        )
        unknown_button.grid(
            row=1,
            column=0,
        )

        known_button = Button(
            image=self._images["right_image"],
            highlightthickness=0,
            relief="flat",
            bg=LexiUi.BACKGROUND_COLOR,
        )
        known_button.grid(row=1, column=1)
        self._ui.set_unknown_button(unknown_button)
        self._ui.set_known_button(known_button)
        return unknown_button, known_button




