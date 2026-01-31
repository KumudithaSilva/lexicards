import csv
import os
import sys
from abc import ABC, abstractmethod
from typing import List

from lexicards.errors.error import DataCorruptionError, DataFileNotFoundError
from lexicards.interfaces.data.i_data_retriever import IDataRetriever


# --------------------------
# Concrete Data Retrievers
# --------------------------
class CSVDataRetriever(IDataRetriever):
    """
    Concrete implementation of IDataRetriever for CSV files.

    Attributes:
        filename (str): Path to the CSV file to load data from.
    """

    def __init__(self, filename: str = "japanese_words.csv"):
        """
        Initialize the CSVDataRetriever with a filename.

        Args:
            filename (str): Path to the CSV file. Defaults to 'data/japanese_words.csv'.
        """
        if hasattr(sys, "_MEIPASS"):
            self.filename = os.path.join(sys._MEIPASS, "assets", "data")
        else:
            self.filename = os.path.join(
                os.path.dirname(__file__), "..", "assets", "data", filename
            )

    def load_data(self) -> List[List[str]]:
        """
        Load data from the CSV file.

        Returns:
            List[List[str]]: List of word entries from the CSV.

        Raises:
            DataFileNotFoundError: If the CSV file does not exist.
            DataCorruptionError: If the CSV file cannot be read or is corrupted.
        """
        if not os.path.isfile(self.filename):
            raise DataFileNotFoundError(f"File not found: {self.filename}")

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                return list(reader)
        except csv.Error:
            raise DataCorruptionError(f"CSV corrupted in {self.filename}")


# --------------------------
# Factory Interface
# --------------------------
class DataRetrieverFactory(ABC):
    """
    Abstract Factory interface for creating IDataRetriever instances.
    """

    @abstractmethod
    def create_data_retriever(self, filename: str) -> IDataRetriever:
        """
        Create and return an IDataRetriever instance.

        Args:
            filename (str): Path to retrieve Data.

        Returns:
            IDataRetriever: Concrete implementation of data retriever.
        """
        pass


# --------------------------
# Concrete Factory
# --------------------------
class CSVDataRetrieverFactory(DataRetrieverFactory):
    """
    Factory for creating CSVDataRetriever instances.
    """

    def create_data_retriever(self, filename: str) -> IDataRetriever:
        """
        Create and return a CSVDataRetriever instance using the configured filename.

        Args:
            filename (str): Path to retrieve CSV file.

        Returns:
            CSVDataRetriever: New instance of CSVDataRetriever.
        """
        return CSVDataRetriever(filename)
