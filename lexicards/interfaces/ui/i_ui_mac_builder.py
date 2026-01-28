from abc import abstractmethod

from lexicards.interfaces.ui.i_ui_builder import IUiBuilder


class IUiBuilderMac(IUiBuilder):
    """Interface for Mac builders with audio support."""

    def build_window(self):
        pass

    def build_canvas(self):
        pass

    def build_title_text(self):
        pass

    def build_buttons(self):
        pass

    def get_ui(self):
        pass

    @abstractmethod
    def build_audio_button(self):
        """Adds audio playback button to the UI."""
        pass
