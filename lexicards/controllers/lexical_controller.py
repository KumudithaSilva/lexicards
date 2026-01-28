import random

from lexicards.controllers.data_retriever import IDataRetriever
from lexicards.interfaces.controller.i_controller import IController
from lexicards.interfaces.ui.i_ui_manager import IUiManager


class LexicalController(IController):
    """
    Controller that connects the UI and random word generator.

    Attributes:
        ui (IUiManager): The UI manager instance to interact with.
        csv_data (IDataRetriever): Loaded CSV file data.
        words (list): List of word pairs loaded from CSV.
        current_index (int): Index of the current random word.
        foreign_language (str): Foreign language label.
        native_language (str): Native language label.
    """

    def __init__(self, ui: IUiManager, csv_data: IDataRetriever):
        """
        Initialize the LexicalController.

        Args:
            ui (IUiManager): UI manager instance to handle user interface interactions.
            csv_data (IDataRetriever): Instance responsible for loading CSV data.
        """
        self.ui = ui
        self.csv_data = csv_data

        self.words = None
        self.current_index = None
        self.foreign_language = None
        self.native_language = None

        self._load_words_if_needed()

    # ----------------------------------------------------------------------
    # Public Button Handlers
    # ----------------------------------------------------------------------

    def start_first_word(self):
        """Generate the initial random word when the app starts."""
        self._generate_random_word()

    def handle_known_word(self):
        """
        Handle the 'Known' button click.

        Displays the meaning of the current word for 3 seconds,
        then automatically generates a new random word.
        """
        self._meaning_of_random_word()
        self.ui.run_after(2000, self._generate_random_word)

    def handle_unknown_word(self):
        """
        Handle the 'Unknown' button click.

        Displays the meaning of the unknown word for 3 seconds,
        then automatically generates a new random word.
        """
        self._meaning_of_random_word()
        self.ui.run_after(2000, self._generate_random_word)

    def handle_next_word(self):
        """
        Handle the 'Next' button click.

        Generates and displays a new random word.
        """
        self._generate_random_word()

    def generate_word_meaning(self):
        """
        Display the meaning of the currently displayed random word.
        """
        self._meaning_of_random_word()

    # ----------------------------------------------------------------------
    # Private Utility Methods
    # ----------------------------------------------------------------------

    def _load_words_if_needed(self):
        """
        Load words from CSV once and initialize the UI with language labels.
        """
        if self.words is None:
            self.words = self.csv_data.load_data()

            if not self.words or len(self.words[0]) < 2:
                raise ValueError("CSV data must contain at least two columns per row.")

            self.foreign_language = self.words[0][0]
            self.native_language = self.words[0][1]

            self.ui.initialize_ui(self.foreign_language, self.native_language)

    def _generate_random_word(self):
        """
        Generate and display a random word from the loaded CSV data.
        """
        if not self.words:
            self.ui.update_word_display("No data loaded.")
            return

        self.current_index = random.randrange(len(self.words))
        random_word = self.words[self.current_index][0]

        self.ui.update_canvas()
        self.ui.update_title(self.foreign_language)
        self.ui.update_word_display(random_word)

    def _meaning_of_random_word(self):
        """
        Fetch and display the meaning of the currently selected word.
        """
        if not self.words:
            self.ui.update_word_display("No data loaded.")
            return

        if self.current_index is None:
            self.ui.update_word_display('')
            return

        self.ui.reset_canvas()
        meaning = self.words[self.current_index][1]
        self.ui.update_title(self.native_language)
        self.ui.update_word_display(meaning)
