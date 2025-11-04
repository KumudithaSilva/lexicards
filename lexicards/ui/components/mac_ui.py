from tkinter import Button

from lexicards.interfaces.ui.i_ui_mac import IUiMac
from lexicards.ui.builders.desktop_ui_builder import DesktopLexiUI


class MacLexiUI(DesktopLexiUI, IUiMac):
    """Mac-specific UI Builder extending Desktop version."""

    def __init__(self, root):
        super().__init__(root)
        self._audio_button = None
        self._audio_callback = None

    # -----------------------------
    # Canvas & Layout Overrides
    # -----------------------------
    def build_canvas(self, card_front_image):
        """Override to adjust grid layout for Mac."""
        canvas = super().build_canvas(card_front_image)
        canvas.grid(row=0, column=0, columnspan=3)  # changed for Mac layout

    # -----------------------------
    # Buttons Overrides
    # -----------------------------
    def build_buttons(self, wrong_image, right_image):
        """Create Known and Unknown buttons."""
        unknown_button, known_button = super().build_buttons(wrong_image, right_image)
        unknown_button.grid(row=1, column=0)
        known_button.grid(row=1, column=2)

    # -----------------------------
    # Mac-only Features
    # -----------------------------
    def build_audio_button(self, audio_image):
        """Add an extra audio button for Mac layout."""
        self._audio_button = Button(
            image=audio_image,
            highlightthickness=0,
            relief="flat",
            bg=self.BACKGROUND_COLOR,
            command=self._audio_callback,
        )
        self._audio_button.grid(row=1, column=1)

    def set_audio_callback(self, callback):
        """Expose method to attach an audio playback callback."""
        self._audio_callback = callback
        if self._audio_button:
            self._audio_button.config(command=callback)
