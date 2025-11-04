from lexicards.interfaces.ui.i_ui_builder import IUiBuilder
from lexicards.ui.components.desktop_ui import DesktopLexiUI


class DesktopLexiUiBuilder(IUiBuilder):
    """Builder class for assembling Desktop UI."""

    def __init__(self, root, images):
        self._root = root
        self._images = images
        self._ui = DesktopLexiUI(root)

    def build_window(self):
        self._ui.build_window()

    def build_canvas(self):
        self._ui.build_canvas(self._images["card_front_image"])

    def create_title_label(self):
        self._ui.create_title_label()

    def create_word_label(self):
        self._ui.create_word_label()

    def build_title_text(self):
        self._ui.create_title_label()

    def build_word_text(self):
        self._ui.create_word_label()

    def build_buttons(self):
        self._ui.build_buttons(self._images["wrong_image"], self._images["right_image"])

    def get_ui(self):
        return self._ui
