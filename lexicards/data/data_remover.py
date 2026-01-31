import csv
import os
import sys
import threading
from abc import ABC, abstractmethod
from lexicards.interfaces.data.i_data_remove import IDataRemover


# --------------------------
# Concrete Data Remover
# --------------------------
class CSVDataRemover(IDataRemover):
    """
    Concrete implementation of IDataSaver for CSV files.

    Attributes:
        filename (str): CSV file name.
        to_remove (set): Set of words that need to be removed
    """

    def __init__(self, filename: str):
        """
        Initialize the CSV data remover.

        Args:
            filename (str): CSV file name (stored under the data directory)
        """
        self.filename = filename
        self.to_remove = set()
        self._lock = threading.Lock()

        # ==========================================================
        # Resolve file path for PyInstaller or normal execution
        # ==========================================================

        if hasattr(sys, "_MEIPASS"):
            self.filename = os.path.join(sys._MEIPASS, "assets", "data")
        else:
            self.filename = os.path.join(
                os.path.dirname(__file__), "..", "assets", "data", filename
            )


    def remove_word(self, word: str) -> None:
        """
        Immediately remove a word from the CSV file.

        Args:
            word (str): Word to remove.
        """
        if not os.path.isfile(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8", newline="") as file:
            rows = list(csv.reader(file))

        if not rows:
            return

        header = rows[0]
        new_rows = [row for row in rows[1:] if row and row[0] != word]

        with open(self.filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(new_rows)


    def mark_for_removal(self, word: str) -> None:
        """
        Mark a word for later removal (batch deletion).

        Args:
            word (str): Word to mark for removal.
        """
        with self._lock:
            self.to_remove.add(word)


    def flush(self) -> None:
        """
        Apply all marked removals to the CSV file and clear the batch.

        Rewrites the CSV file only once for efficiency.
        """
        with self._lock:
            if not self.to_remove or not os.path.isfile(self.filename):
                return
            rows_to_remove = self.to_remove.copy()
            self.to_remove.clear()

        with open(self.filename, "r", encoding="utf-8", newline="") as file:
            rows = list(csv.reader(file))
            print(len(rows))

        if not rows:
            return

        header = rows[0]
        new_rows = [
            row for row in rows[1:]
            if row and row[0] not in rows_to_remove
        ]
        print(len(new_rows))

        with open(self.filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(new_rows)

        print("flush end")


    def flush_async(self) -> None:
        """Run flush in a background thread."""
        threading.Thread(
            target=self.flush,
            daemon=True
        ).start()

# --------------------------
# Factory Interface
# --------------------------
class DataRemoverFactory(ABC):
    """
    Abstract Factory interface for deleting IDataRemover instances.
    """

    @abstractmethod
    def create_data_remover(self, filename: str) -> IDataRemover:
        """
        Create and return an IDataRemover instance.

        Args:
            filename (str): Path to the target storage.

        Returns:
            IDataRemover: Concrete implementation of data remover.
        """
        pass


# --------------------------
# Concrete Factory
# --------------------------
class CSVDataRemoverFactory(DataRemoverFactory):
    """
    Factory for creating CSVDataRemover instances.
    """

    def create_data_remover(self, filename: str) -> IDataRemover:
        """
        Create and return a CSVDataRemover instance.

        Args:
            filename (str): Path to the CSV file.

        Returns:
            CSVDataRemover: A new CSV data remover.
        """
        return CSVDataRemover(filename)
