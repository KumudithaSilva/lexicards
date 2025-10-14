from tkinter import Canvas, Button


class LexiUI:
    """
    A  Tkinter-based UI for LexiCards.

    Responsibilities:
        - Render all UI elements: logo canvas, labels, buttons
        - Expose public API for retrieving and setting entry values
        - Allow setting callback for the buttons

    Attributes:
        _root (Tk): Main Tkinter application window.
        _images (dict): Dictionary of Tkinter PhotoImage objects.
        _canvas (Canvas): Canvas for logo or graphics.
        _known_button (Button): Button to mark that input data is familiar.
        _unknown_button (Button): Button to mark that input data is unfamiliar.
    """

    BACKGROUND_COLOR = "#B1DDC6"
    LABEL_TOP_FONT = ("Arial", 40, "italic")
    LABEL_BOTTOM_FONT = ("Arial", 60, "italic")

    def __init__(self, root, images=None, known_callback=None, unknown_callback=None):
        """
        Initialize the LexiCards.

        Args:
            root (Tk): The main Tkinter window.
            images (dict, optional): Dictionary containing 'main_logo' and 'main_icon'.
            known_callback (callable, optional): Function to call when known button is clicked.
            unknown_callback (callable, optional): Function to call when unknown button is clicked.

        """
        self._root = root
        self._images = images or {}
        self._known_button = None
        self._unknown_button = None

        # Wire callbacks after widgets are created
        self._build_ui()

        # Wire callbacks after widgets are created
        if known_callback:
            self.set_known_callback(known_callback)
        else:
            self.set_unknown_callback(unknown_callback)

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
        self._title_text_id = self._canvas.create_text(400, 150, text="Title", font=self.LABEL_TOP_FONT)
        self._word_text_id = self._canvas.create_text(400, 263, text="word", font=self.LABEL_BOTTOM_FONT)

        self._canvas.grid(row=0, column=0, columnspan=2)

        # Button configuration
        self._unknown_button = Button(
            image=self._images["wrong_image"], highlightthickness=0
        )
        self._unknown_button.grid(
            row=1,
            column=0,
        )

        self._known_button = Button(
            image=self._images["right_image"], highlightthickness=0
        )
        self._known_button.grid(row=1, column=1)

    # -----------------------------
    # Public getters
    # -----------------------------
    def get_title_text(self) -> str:
        """Returns the current text of the title label."""
        return self._canvas.itemcget(self._title_text_id, "text")

    def get_word_text(self) -> str:
        """Returns the current text of the word label."""
        return self._canvas.itemcget(self._word_text_id, "text")

    # -----------------------------
    # Public setters
    # -----------------------------
    def set_title(self, title: str):
        """Sets the text of the title label."""
        self._canvas.itemconfig(self._title_text_id, text=title)

    def set_word(self, title: str):
        """Sets the text of the word label."""
        self._canvas.itemconfig(self._word_text_id, text=title)


    # -----------------------------
    # Public method to set the known button callback dynamically
    # -----------------------------
    def set_known_callback(self, callback):
        """
        Set or update the known button callback.

        Args:
            callback (callable): Function to call when button is clicked.
        """
        self._known_button.config(command=callback)

    # -----------------------------
    # Public method to set the unknown button callback dynamically
    # -----------------------------
    def set_unknown_callback(self, callback):
        """
        Set or update the unknown button callback.

        Args:
            callback (callable): Function to call when unknown button is clicked.
        """
        self._unknown_button.config(command=callback)
