from lexicards.core.singleton_meta import SingletonMeta
from lexicards.interfaces.ui.i_ui_manager import IUiManager


class UiManager(IUiManager, metaclass=SingletonMeta):
    """Handles UI state initialization and dynamic updates."""

    def __init__(self, ui):
        self._ui = ui

    def initialize_ui(self, foreign_language: str, native_language: str):
        """Set up the initial UI view."""
        self._ui.set_title(foreign_language)
        self._ui.set_word(native_language)

    def update_word_display(self, word: str):
        """Update the displayed word."""
        self.rest_word_display()
        self._ui.set_word(word)

    def update_title(self, title: str):
        """Change the title text."""
        self.rest_title()
        self._ui.set_title(title)

    def rest_word_display(self):
        """Reset the displayed word."""
        self._ui.set_word("")

    def rest_title(self):
        """Reset the title."""
        self._ui.set_title("")

    def reset(self):
        """Reset the UI state. Useful in tests or reinitialization."""
        self._ui = None
