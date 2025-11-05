import random

from lexicards.controllers.data_retriever import IDataRetriever
from lexicards.interfaces.controller.i_controller import IController
from lexicards.interfaces.ui.i_ui_manager import IUiManager


class LexicalController(IController):
    """
    Controller class that connects the UI and random word generator.

    Attributes:
        ui (IUiManager): The UI manager instance to interact with.
        csv_data (IDataRetriever): Loaded CSV file data.
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
        self._load_words_if_needed()

    def generate_random_new_word(self):
        """
        Handle the 'Known' button click by generating a new random word.
        """
        self._generate_random_word()

    def generate_random_unknown_word(self):
        """
        Handle the 'Unknown' button click by generating a new random word.
        """
        self._generate_random_word()

    def generate_word_meaning(self):
        """Generate the random word's meaning."""
        self._meaning_of_random_word()


    def _load_words_if_needed(self):
        """
        Load words from CSV only once and cache them.
        """
        if self.words is None:
            self.words = self.csv_data.load_data()

    def _generate_random_word(self):
        """
        Generate and display a random word from the loaded CSV data.
        """
        words = self.words

        if not words:
            self.ui.update_word_display("No data loaded.")
            return

        self.current_index = random.randrange(len(words))

        random_word = words[self.current_index][0]
        self.ui.update_title("Japanese")
        self.ui.update_word_display(random_word)

    def _meaning_of_random_word(self):
        """
        Fetch and display meaning of the currently selected word.
        """
        words = self.words

        if not words:
            self.ui.update_word_display("No data loaded.")
            return

        if self.current_index is None:
            self.ui.update_word_display('')
            return

        meaning = words[self.current_index][1]
        self.ui.update_title("English")
        self.ui.update_word_display(meaning)
