from abc import ABC, abstractmethod


class IUiDirector(ABC):
    """Interface for directing the build sequence of the UI."""

    @abstractmethod
    def construct_ui(self):
        """Assemble all parts of the UI using the builder."""
        pass
