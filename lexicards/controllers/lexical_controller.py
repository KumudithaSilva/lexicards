import os.path
import random
from typing import List

from lexicards.controllers.data_retriever import DataRetrieverFactory
from lexicards.controllers.data_saver import DataSaverFactory
from lexicards.interfaces.controller.i_controller import IController
from lexicards.interfaces.ui.i_ui_manager import IUiManager


class LexicalController(IController):
    """
    Controller that connects the UI and random word generator.

    Attributes:
        ui (IUiManager): The UI manager instance to interact with.
        csv_data (DataRetrieverFactory): Factory for creating IDataRetriever instances.
        saver_factory (DataSaverFactory): Factory for creating IDataSaver instances.
        words (list[list[str]]): List of word pairs loaded from CSV.
        current_index (int | None): Index of the currently selected random word.
        foreign_language (str | None): Foreign language label.
        native_language (str | None): Native language label.
        random_word (str | None): Currently selected random word.
        meaning_word (str | None): Meaning of the currently selected word.
    """

    def __init__(
        self,
        ui: IUiManager,
        csv_data: DataRetrieverFactory,
        saver_factory: DataSaverFactory,
    ):
        """
        Initialize the LexicalController.

        Args:
            ui (IUiManager): UI manager instance to handle user interface interactions.
            csv_data (DataRetrieverFactory): Factory for creating IDataRetriever instances.
            saver_factory (DataSaverFactory): Factory for creating IDataSaver instances.
        """
        self.ui = ui
        self.csv_data = csv_data
        self.saver_factory = saver_factory
        self.words: list[list[str]] | None = None
        self.current_index: int | None = None
        self.foreign_language: str | None = None
        self.native_language: str | None = None
        self.random_word: str | None = None
        self.meaning_word: str | None = None

        self._load_words_if_needed()

    # ----------------------------------------------------------------------
    # Public Button Handlers
    # ----------------------------------------------------------------------

    def start_first_word(self) -> None:
        """Generate and display the initial random word when the app starts."""
        self._generate_random_word()

    def handle_known_word(self) -> None:
        """
        Handle the 'Known' button click.

        Displays the meaning of the current word for 2 seconds,
        then automatically generates a new random word.
        Save the word to the known words file.
        """
        self._meaning_of_random_word()
        self.ui.run_after(2000, self._generate_random_word)
        # self._save_to_file(filename="data/known_words.csv")

    def handle_unknown_word(self) -> None:
        """
        Handle the 'Unknown' button click.

        Displays the meaning of the current word for 2 seconds,
        then automatically generates a new random word.
        Save the word to the unknown words file.
        """
        self._meaning_of_random_word()
        self.ui.run_after(2000, self._generate_random_word)
        # self._save_to_file(filename="data/unknown_words.csv")

    def handle_next_word(self) -> None:
        """Handle the 'Next' button click by generating a new random word."""
        self._generate_random_word()

    def generate_word_meaning(self) -> None:
        """Display the meaning of the currently displayed random word."""
        self._meaning_of_random_word()

    # ----------------------------------------------------------------------
    # Private Utility Methods
    # ----------------------------------------------------------------------

    def _load_words_if_needed(self) -> None:
        """
        Load words from the CSV file once and initialize the UI with language labels.

        Raises:
            ValueError: If the CSV does not contain at least two columns per row.
        """
        if self.words is None:
            self.words = self._load_data("japanese_words.csv")

            if not self.words or len(self.words[0]) < 2:
                raise ValueError("CSV data must contain at least two columns per row.")

            self.foreign_language = self.words[0][0]
            self.native_language = self.words[0][1]

            self.ui.initialize_ui(self.foreign_language, self.native_language)

    def _generate_random_word(self) -> None:
        """Generate and display a random word from the loaded CSV data."""
        if not self.words:
            self.ui.update_word_display("No data loaded.")
            return

        self.current_index = random.randrange(len(self.words))
        self.random_word = self.words[self.current_index][0]

        self.ui.update_canvas()
        self.ui.update_title(self.foreign_language)
        self.ui.update_word_display(self.random_word)

    def _meaning_of_random_word(self) -> None:
        """Fetch and display the meaning of the currently selected word."""
        if not self.words or self.current_index is None:
            self.ui.update_word_display("")
            return

        self.meaning_word = self.words[self.current_index][1]
        self.ui.reset_canvas()
        self.ui.update_title(self.native_language)
        self.ui.update_word_display(self.meaning_word)

    def _save_to_file(self, filename: str) -> None:
        """Save the current random word and its meaning to the given file."""
        if self.random_word is None or self.meaning_word is None:
            return

        saver = self.saver_factory.create_data_saver(filename)

        if not os.path.isfile(filename):
            saver.save_data(self.foreign_language, self.native_language)

        saver.save_data(self.random_word, self.meaning_word)

    def _load_data(self, filename: str) -> List[List[str]]:
        """Load word data from a CSV file using the configured data retriever."""
        retriever = self.csv_data.create_data_retriever(filename)
        return retriever.load_data()
