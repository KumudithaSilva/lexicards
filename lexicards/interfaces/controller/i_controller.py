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
        """Called when the user clicks the 'next' button.
        Display the next random word and show its meaning after three seconds."""
        pass

    @abstractmethod
    def handle_speak(self):
        """Called when the user clicks the 'Speak' button."""
        pass
