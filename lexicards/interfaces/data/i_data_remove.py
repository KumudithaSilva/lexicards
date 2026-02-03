from abc import ABC, abstractmethod


class IDataRemover(ABC):
    """Interface for removing words from storage."""

    @abstractmethod
    def remove_word(self, word: str) -> None:
        """Immediately remove the given word from storage."""
        pass

    @abstractmethod
    def mark_for_removal(self, word: str) -> None:
        """Mark a word for later removal (batch removal)."""
        pass

    @abstractmethod
    def flush(self) -> None:
        """Apply all marked removals to the storage."""
        pass

    @abstractmethod
    def flush_async(self):
        """Apply all threading for flush."""
        pass
