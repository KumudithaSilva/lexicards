import random
from lexicards.controllers.data_retriever import IDataRetriever
from lexicards.interfaces.i_controller import IController
from lexicards.interfaces.i_ui import IUI


class LexicalController(IController):
    """
    Controller class that connects the UI and random word generator.

    Attributes:
        ui (LexiUI): The UI instance to interact with.
        csv_data (DataRetriever): Loaded CSV file data.
    """

    def __init__(self, ui: IUI, csv_data: IDataRetriever):
        """
        Initialize the LexicalController.

        Args:
            ui (LexiUI): LexiUI instance to handle user interface interactions.
            csv_data (DataRetriever): Instance responsible for loading CSV data.
        """
        self.ui = ui
        self.csv_data = csv_data

        # Wire the buttons to controller methods
        self.ui.set_known_callback(self.generate_random_new_word)
        self.ui.set_unknown_callback(self.generate_random_unknown_word)

        # Initialize UI
        self.ui.set_title("Japanese")
        self.ui.set_word("")

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

        random_word = self.pick_random_word(words)
        self.ui.set_word(random_word)

    # --------------------------
    # Static Helper Methods
    # --------------------------

    @staticmethod
    def pick_random_word(word_list):
        """
        Pick a random word from a given list.

        Args:
            word_list (list): List of words.

        Returns:
            str: Random word from the list.
        """
        if not word_list:
            return None, None
        index = random.randint(0, len(word_list) - 1)
        random_word = word_list[index][0]
        return random_word