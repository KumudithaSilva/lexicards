from abc import abstractmethod

from lexicards.interfaces.ui.components.i_ui_base import IUiBase


class IUiMac(IUiBase):
    """Mac UI contract with audio support."""

    def set_title(self, title: str):
        pass

    def set_word(self, word: str):
        pass

    def get_title_text(self) -> str:
        pass

    def get_word_text(self) -> str:
        pass

    def set_known_callback(self, callback):
        pass

    def set_unknown_callback(self, callback):
        pass

    def set_next_callback(self, callback):
        pass

    @abstractmethod
    def set_audio_callback(self, callback):
        pass
