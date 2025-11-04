from abc import ABC, abstractmethod


class IUiManager(ABC):
    """Interface for managing UI updates and managing initialization."""

    @abstractmethod
    def initialize_ui(self):
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
    def reset(self):
        """Reset the UI state."""
        pass
