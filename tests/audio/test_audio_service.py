import unittest
from unittest.mock import MagicMock

from lexicards.controllers.lexical_controller import LexicalController
from lexicards.interfaces.audio.i_audio_servcie import IAudioService


class TestAudioServices(unittest.TestCase):
    def test_handle_speak_calls_audio(self):
        audio_mock: IAudioService = MagicMock(spec=IAudioService)
        ui_mock = MagicMock()
        manager_mock = MagicMock()
        manager_mock.foreign_language = "ja"

        controller = LexicalController(ui_mock, manager_mock, audio_mock)
        controller.current_word = "こんにちは"

        controller.handle_speak()

        # Assert that speak_async was called on the interface
        audio_mock.speak_async.assert_called_once_with("こんにちは", "ja")


if __name__ == "__main__":
    unittest.main()
