import csv
import os
import sys
from abc import ABC, abstractmethod

from lexicards.errors.error import DataCorruptionError
from lexicards.interfaces.data.i_data_saver import IDataSaver


# --------------------------
# Concrete Data Saver
# --------------------------
class CSVDataSaver(IDataSaver):
    """
    Concrete implementation of IDataSaver for CSV files.

    Attributes:
        filename (str): CSV file name.
        header (tuple[str, str]): Column headers.
        existing_words (set): Set of words already saved to avoid duplicates.
    """

    def __init__(self, filename: str, header: tuple[str, str]):
        """
        Initialize the CSV data saver.

        Args:
            filename (str): CSV file name (stored under the data directory)
            header (tuple[str, str]): Column headers (e.g. ("Japanese", "English"))
        """
        self.header = header
        self.filename = filename
        self.existing_words = set()

        # ==========================================================
        # Resolve file path for PyInstaller or normal execution
        # ==========================================================

        if hasattr(sys, "_MEIPASS"):
            self.filename = os.path.join(sys._MEIPASS, "assets", "data")
        else:
            self.filename = os.path.join(
                os.path.dirname(__file__), "..", "assets", "data", filename
            )

        # ==========================================================
        # Load existing words to prevent duplicates
        # ==========================================================

        if os.path.isfile(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8", newline="") as file:
                    reader = csv.reader(file)
                    next(reader, None)  # Skip header

                    for row in reader:
                        if row:
                            self.existing_words.add(row[0])
            except (csv.Error, OSError) as exc:
                raise DataCorruptionError(
                    f"Cannot read existing CSV: {self.filename}"
                ) from exc

    def save_data(self, word: str, meaning: str) -> None:
        """
        Save data to the CSV file.

        Args:
            word (str): Foreign-language word
            meaning (str): Translated meaning

        Raises:
            DataCorruptionError: If the CSV file cannot be written or is corrupted.
        """
        if word in self.existing_words:
            return

        try:
            file_exists = os.path.isfile(self.filename)
            with open(self.filename, "a", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)

                if not file_exists:
                    writer.writerow(self.header)

                writer.writerow([word, meaning])
        except csv.Error:
            raise DataCorruptionError(f"Cannot write to CSV: {self.filename}")


# --------------------------
# Factory Interface
# --------------------------
class DataSaverFactory(ABC):
    """
    Abstract Factory interface for creating IDataSaver instances.
    """

    @abstractmethod
    def create_data_saver(self, filename: str) -> IDataSaver:
        """
        Create and return an IDataSaver instance.

        Args:
            filename (str): Path to the target storage.

        Returns:
            IDataSaver: Concrete implementation of data saver.
        """
        pass


# --------------------------
# Concrete Factory
# --------------------------
class CSVDataSaverFactory(DataSaverFactory):
    """
    Factory for creating CSVDataSaver instances.
    """
    def __init__(self, foreign_language: str, native_language: str):
        """
        Initialize the factory with language metadata.

        Args:
            foreign_language (str): Source language
            native_language (str): Target language
        """
        self.header = (foreign_language, native_language)

    def create_data_saver(self, filename: str) -> IDataSaver:
        """
        Create and return a CSVDataSaver instance.

        Args:
            filename (str): Path to the CSV file.

        Returns:
            CSVDataSaver: A new CSV data saver.
        """
        return CSVDataSaver(filename, self.header)
