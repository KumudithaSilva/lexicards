from abc import ABC, abstractmethod


class IController(ABC):
    """Interface for LexicalController types."""

    @abstractmethod
    def generate_random_new_word(self):
        """Handle logic when a user clicks the 'Known' button."""
        pass

    @abstractmethod
    def generate_random_unknown_word(self):
        """Handle logic when a user clicks the 'Unknown' button."""
        pass
