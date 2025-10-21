from abc import ABC, abstractmethod
from typing import List

class IDataRetriever(ABC):
    """Interface for any data retriever (CSV, DB, API)."""

    @abstractmethod
    def load_data(self) -> List[List[str]]:
        """Return list of word entries."""
        pass
