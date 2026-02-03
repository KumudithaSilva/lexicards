from lexicards.interfaces.audio.i_audio_servcie import IAudioService
from lexicards.interfaces.controller.i_controller import IController
from lexicards.interfaces.manager.i_manager import IWordManager
from lexicards.interfaces.ui.manager.i_ui_manager import IUiManager


class LexicalController(IController):
    """
    Controller that connects the UI and word manager, handling user interactions.

    Attributes:
        ui (IUiManager): The UI manager instance for interface updates.
        manager (IWordManager): The word manager instance for vocabulary words manage.
        audio (IAudioService): The audio service instance for text-to-speech.
        current_word (str | None): The currently displayed word.
        current_meaning (str | None): The meaning of the current word.
    """

    def __init__(self, ui: IUiManager, manager: IWordManager, audio: IAudioService):
        """
        Initialize the LexicalController with UI, word manager, and audio service.

        Args:
            ui (IUiManager): UI manager instance for interface interactions.
            manager (IWordManager): Word manager instance for managing vocabulary words.
            audio (IAudioService): Audio service instance for text-to-speech functionality.
        """
        self.ui = ui
        self.manager = manager
        self.audio = audio
        self.current_word = None
        self.current_meaning = None

        self.ui.initialize_ui(
            self.manager.foreign_language, self.manager.native_language
        )

    # ----------------------------------------------------------------------
    # Public Button Handlers
    # ----------------------------------------------------------------------

    def start_first_word(self) -> None:
        """Generate and display the initial random word when the app starts."""
        self.handle_next_word()

    def handle_known_word(self) -> None:
        """
        Handle the 'Known' button click.
        Mark the current word as known and update storage.
        """
        self.manager.mark_as_known()

    def handle_unknown_word(self) -> None:
        """
        Handle the 'Unknown' button click.
        Mark the current word as unknown and update storage.
        """
        self.manager.mark_as_unknown()

    def handle_next_word(self) -> None:
        """Display the next random word and show its meaning after three seconds."""
        try:
            word, meaning = self.manager.get_random_word()
            self.current_word = word
            self.current_meaning = meaning

            self.ui.update_canvas()
            self.ui.update_title(self.manager.foreign_language)
            self.ui.update_word_display(word)

            self.ui.run_after(3000, self._display_meaning)

        except ValueError:
            self.ui.update_word_display("No data loaded.")

    def handle_speak(self):
        """Generate text to speak."""
        self.audio.speak_async(self.current_word, self.manager.foreign_language)

    # ----------------------------------------------------------------------
    # Private Utility Methods
    # ----------------------------------------------------------------------

    def _display_meaning(self) -> None:
        """Display the meaning of the current word on the UI."""
        if self.current_word is None or self.current_meaning is None:
            self.ui.update_word_display("")
            return

        self.ui.reset_canvas()
        self.ui.update_title(self.manager.native_language)
        self.ui.update_word_display(self.current_meaning)
