import csv
import os
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
        filename (str): Path to the CSV file to save data to.
    """

    def __init__(self, filename: str):
        """
        Initialize the CSVDataSaver with a filename.

        Args:
            filename (str): Path to the CSV file where data will be saved.
        """
        self.filename = filename


    def save_data(self, word: str, meaning: str) -> None:
        """
        Save data to the CSV file.

        Raises:
            DataCorruptionError: If the CSV file cannot be written or is corrupted.
        """
        try:
            with open(self.filename, "a", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
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

    def create_data_saver(self, filename: str) -> IDataSaver:
        """
        Create and return a CSVDataSaver instance.

        Args:
            filename (str): Path to the CSV file.

        Returns:
            CSVDataSaver: A new CSV data saver.
        """
        return CSVDataSaver(filename)