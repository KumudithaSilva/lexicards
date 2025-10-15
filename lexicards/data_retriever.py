import csv
import os.path
from lexicards.errors import DataFileNotFoundError, DataCorruptionError


class DataRetriever:
    """
    Retrieve csv file.

    Attribute:
        filename(str): Path to the CSV file where data is stored.
    """

    def __init__(self, filename="data/japanese_words.csv"):
        self.filename = filename
        self.data = []

    # --------------------------
    # Data load  Methods
    # --------------------------

    def load_data(self):
        """
        Retrieve data from the CSV file.

        Returns:
            list: Existing data or an empty list if the file is not found.

        Raises:
            DataCorruptionError: If the CSV file is corrupted or unreadable.
            DataFileNotFoundError: If the file does not exist.
        """
        if not os.path.isfile(self.filename):
            raise DataFileNotFoundError(f"File not found: {self.filename}")

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                self.data = list(reader)
            return self.data
        except csv.Error:
            raise DataCorruptionError(f"CSV corrupted in {self.filename}")
