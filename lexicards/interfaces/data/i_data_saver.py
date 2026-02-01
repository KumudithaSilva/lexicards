from abc import ABC, abstractmethod


class IDataSaver(ABC):
    """Interface for saving vocabulary data (CSV, DB, API)."""

    @abstractmethod
    def save_data(self, word: str, meaning: str) -> None:
        """
        Save a single word and its meaning.

        Args:
            word (str): The foreign word.
            meaning (str): The translated meaning.
        """
        pass
