from abc import ABC, abstractmethod
from typing import Tuple


class IWordManager(ABC):
    """Interface for managing vocabulary words."""

    @abstractmethod
    def get_random_word(self) -> Tuple[str, str]:
        """Return a random word and its meaning."""
        pass

    @abstractmethod
    def mark_as_known(self) -> None:
        """Mark the current word as known and update storage."""
        pass

    @abstractmethod
    def mark_as_unknown(self) -> None:
        """Mark the current word as unknown and update storage."""
        pass

    @property
    @abstractmethod
    def foreign_language(self) -> str:
        """Return the foreign language label."""
        pass

    @property
    @abstractmethod
    def native_language(self) -> str:
        """Return the native language label."""
        pass
