from abc import ABC, abstractmethod


class IController(ABC):
    """Interface for word-learning controller behavior."""

    @abstractmethod
    def start_first_word(self):
        """Initial random word display when the application starts."""
        pass

    @abstractmethod
    def handle_known_word(self):
        """Called when the user clicks the 'Known' button.
        Marks the current word as known and shows a new random word."""
        pass

    @abstractmethod
    def handle_unknown_word(self):
        """Called when the user clicks the 'Unknown' button.
        Marks the current word as unknown and shows a new random word."""
        pass

    @abstractmethod
    def handle_next_word(self):
        """Called when the user clicks the 'Next' button.
        Moves to the next random word, regardless of known/unknown state."""
        pass

    @abstractmethod
    def generate_word_meaning(self):
        """Generates or fetches the meaning of the currently displayed word."""
        pass
