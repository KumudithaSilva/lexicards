import random

from lexicards.controllers.data_retriever import IDataRetriever
from lexicards.interfaces.controller.i_controller import IController
from lexicards.interfaces.ui.i_ui_base import IUiBase


class LexicalController(IController):
    """
    Controller class that connects the UI and random word generator.

    Attributes:
        ui (LexiUI): The UI instance to interact with.
        csv_data (DataRetriever): Loaded CSV file data.
    """

    def __init__(self, ui: IUiBase, csv_data: IDataRetriever):
        """
        Initialize the LexicalController.

        Args:
            ui (LexiUI): LexiUI instance to handle user interface interactions.
            csv_data (DataRetriever): Instance responsible for loading CSV data.
        """
        self.ui = ui
        self.csv_data = csv_data

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

    def _generate_random_word(self):
        """
        Generate and display a random word from the loaded CSV data.
        """
        words = self.csv_data.load_data()

        if not words:
            self.ui.set_word("No data loaded.")
            return

        random_word = random.choice(words)[0]
        self.ui.set_word(random_word)
