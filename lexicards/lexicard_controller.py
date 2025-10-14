import csv
import random

from lexicards.ui import LexiUI


class LexicalController:
    """
    Controller class that connects the UI,
    random word generator.

    Attributes:
        ui (LexiUI): The UI instance to interact with.
        data (list): Loaded word data from the CSV file.
        random_number (int): Index of the currently selected word.
    """

    def __init__(self, ui: LexiUI):
        """
        Initialize the LexicalController.

        Args:
            ui: Lexicards instance to get entry values.

        """
        self.ui = ui
        self.data = []
        self.random_number = None

        self.load_data()

        # Wire the Generate Password and Add buttons to controller method
        self.ui.set_known_callback(self.generate_random_new_word)
        self.ui.set_unknown_callback(self.generate_random_new_word)

        self.ui.set_title("Japanese")
        self.ui.set_word("")


    def load_data(self):
        """
        Load word data from the CSV file.
        """
        try:
            with open("data/japanese_words.csv", "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                self.data = list(reader)

        except FileNotFoundError:
            print("Error: 'japanese_words.csv' not found.")
            self.data = []
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            self.data = []

    def generate_random_new_word(self):
        """
        Handle the 'known' button click by generating a new word.
        """
        self._set_random_word()

    def generate_random_unknown_word(self):
        """
        Handle the 'unknown' button click by generating a new word.
        """
        self._set_random_word()

    def _set_random_word(self):
        """
        Select a random word from the data and update the UI.
        """
        if not self.data:
            self.ui.set_word("No data loaded.")
            return

        self.random_number = random.randint(0, len(self.data) - 1)
        word = self.data[self.random_number][0]
        self.ui.set_word(word)



