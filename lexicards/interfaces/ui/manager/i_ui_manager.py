from abc import ABC, abstractmethod


class IUiManager(ABC):
    """Interface for managing UI updates and managing initialization."""

    @abstractmethod
    def initialize_ui(self, foreign_language: str, native_language: str):
        """Set the initial UI state."""
        pass

    @abstractmethod
    def update_word_display(self, word: str):
        """Update the displayed word text."""
        pass

    @abstractmethod
    def update_title(self, title: str):
        """Update the UI title text."""
        pass

    @abstractmethod
    def run_after(self, delay_ms: int, callback):
        """Schedule a callback to run after a specified delay."""
        pass

    @abstractmethod
    def update_canvas(self):
        """Update the canvas image and color"""
        pass

    @abstractmethod
    def reset_canvas(self):
        """Reset the canvas image and color"""
        pass

    @abstractmethod
    def rest_title(self):
        """Reset the UI title text."""
        pass

    @abstractmethod
    def rest_word_display(self):
        """Reset the UI word text."""
        pass

    @abstractmethod
    def reset(self):
        """Reset the UI state."""
        pass
