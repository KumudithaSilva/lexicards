import unittest
from unittest.mock import MagicMock

from lexicards.controllers.lexical_controller import LexicalController
from lexicards.interfaces.audio.i_audio_servcie import IAudioService
from lexicards.interfaces.manager.i_manager import IWordManager
from lexicards.interfaces.ui.manager.i_ui_manager import IUiManager


class TestController(unittest.TestCase):
    def setUp(self):
        self.ui = MagicMock(spec=IUiManager)
        self.manager = MagicMock(spec=IWordManager)
        self.audio = MagicMock(spec=IAudioService)

        self.manager.foreign_language = "Japanese"
        self.manager.native_language = "English"

        self.controller = LexicalController(
            ui=self.ui, manager=self.manager, audio=self.audio
        )

    def test_controller_initializes_ui(self):
        self.ui.initialize_ui.assert_called_once_with("Japanese", "English")

    def test_handle_next_word(self):
        self.manager.get_random_word.return_value = ("川", "River")

        self.controller.handle_next_word()

        self.ui.update_canvas.assert_called_once()
        self.ui.update_title.assert_called_with("Japanese")
        self.ui.update_word_display.assert_called_once_with("川")
        self.ui.run_after.assert_called_once()


if __name__ == "__main__":
    unittest.main()
