from lexicards.interfaces.controller.i_controller import IController
from lexicards.interfaces.manager.i_manager import IWordManager
from lexicards.interfaces.ui.manager.i_ui_manager import IUiManager


class LexicalController(IController):
    """
    Controller that connects the UI and random word generator.

    Attributes:
        ui (IUiManager): The UI manager instance to interact with.
    """

    def __init__(
        self,
        ui: IUiManager,
        manager: IWordManager,
    ):
        """
        Initialize the LexicalController.

        Args:
            ui (IUiManager): UI manager instance to handle user interface interactions.
        """
        self.ui = ui
        self.manager = manager
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

        Displays the meaning of the current word for 2 seconds,
        then generates a new random word. Marks the word as known.
        """
        self._display_meaning()
        self.ui.run_after(2000, self.handle_next_word)
        self.manager.mark_as_known()

    def handle_unknown_word(self) -> None:
        """
        Handle the 'Unknown' button click.

        Displays the meaning of the current word for 2 seconds,
        then generates a new random word. Marks the word as unknown.
        """
        self._display_meaning()
        self.ui.run_after(2000, self.handle_next_word)
        self.manager.mark_as_unknown()

    def handle_next_word(self) -> None:
        """Generate and display the next random word."""
        try:
            word, meaning = self.manager.get_random_word()
            self.current_word = word
            self.current_meaning = meaning

            self.ui.update_canvas()
            self.ui.update_title(self.manager.foreign_language)
            self.ui.update_word_display(word)

        except ValueError:
            self.ui.update_word_display("No data loaded.")


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

