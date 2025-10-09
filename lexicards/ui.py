from tkinter import Canvas, Button

class LexiUI:
    """
    A  Tkinter-based UI for LexiCards.

    Responsibilities:
        - Render all UI elements: logo canvas, labels, buttons
        - Expose public API for retrieving and setting entry values
        - Allow setting callback for the buttons

    Attributes:

    """

    BACKGROUND_COLOR = "#B1DDC6"
    LABEL_TOP_FONT = ("Arial", 40, "italic")
    LABEL_BOTTOM_FONT = ("Arial", 60, "italic")

    def __init__(self, root, images=None):
        """
        Initialize the LexiCards.

        Args:
            root (Tk): The main Tkinter window.
            images (dict, optional): Dictionary containing 'main_logo' and 'main_icon'.
        """

        self._root = root
        self._images = images or {}

        self._build_ui()

    def _build_ui(self):
        """UI widgets and layout."""

        # Window configuration
        self._root.title("LexiCards")
        self._root.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)
        self._root.resizable(False, False)

        # Canvas configuration
        self._canvas = Canvas(self._root, width=800, height=526, highlightthickness=0)
        self._canvas.config(background=self.BACKGROUND_COLOR)
        self._canvas.create_image(400, 263, image=self._images["card_front_image"])
        self._canvas.create_text(400, 150, text="Title", font=self.LABEL_TOP_FONT)
        self._canvas.create_text(400, 263, text="word", font=self.LABEL_BOTTOM_FONT)
        self._canvas.grid(row=0, column=0, columnspan=2)

        # Button configuration
        self._unknown_button = Button(image=self._images["wrong_image"], highlightthickness=0)
        self._unknown_button.grid(row=1, column=0,)

        self._known_button = Button(image=self._images["right_image"], highlightthickness=0)
        self._known_button.grid(row=1, column=1)












