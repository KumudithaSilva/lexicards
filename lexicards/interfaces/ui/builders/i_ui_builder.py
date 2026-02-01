from abc import ABC, abstractmethod


class IUiBuilder(ABC):
    """Interface for building UI components step-by-step."""

    @abstractmethod
    def build_window(self):
        """Create the main window."""
        pass

    @abstractmethod
    def build_canvas(self):
        """Create the main canvas."""
        pass

    @abstractmethod
    def build_title_text(self):
        """Create the title label."""
        pass

    @abstractmethod
    def build_buttons(self):
        """Create the Known/Unknown buttons."""
        pass

    @abstractmethod
    def get_ui(self):
        """Return the final constructed UI object."""
        pass
