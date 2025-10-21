from abc import ABC, abstractmethod


class IUI(ABC):
    """Interface for LexiCards User Interfaces."""

    @abstractmethod
    def set_title(self, title: str):
        """Sets the title text."""
        pass

    @abstractmethod
    def set_word(self, word: str):
        """Sets the main word text."""
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
