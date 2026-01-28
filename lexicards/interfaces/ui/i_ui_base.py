from abc import ABC, abstractmethod


class IUiBase(ABC):
    """Interface defining core UI interactions."""

    @abstractmethod
    def set_title(self, title: str):
        """Sets the title text."""
        pass

    @abstractmethod
    def set_word(self, word: str):
        """Sets the main word text."""
        pass

    @abstractmethod
    def set_canvas_image(self, image):
        """Change the canvas image."""
        pass

    @abstractmethod
    def set_canvas_color(self, color: str):
        """Change canvas background color."""
        pass

    @abstractmethod
    def get_title_text(self) -> str:
        """Returns the current title text."""
        pass

    @abstractmethod
    def get_word_text(self) -> str:
        """Returns the current word text."""
        pass

    @abstractmethod
    def set_known_callback(self, callback):
        """Sets the callback for 'known' button."""
        pass

    @abstractmethod
    def set_unknown_callback(self, callback):
        """Sets the callback for 'unknown' button."""
        pass

    @abstractmethod
    def set_next_callback(self, callback):
        """Sets the callback for 'next' button."""
        pass
