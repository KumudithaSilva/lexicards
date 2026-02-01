import random
from typing import List, Tuple

from lexicards.data.data_remover import DataRemoverFactory
from lexicards.data.data_retriever import DataRetrieverFactory
from lexicards.data.data_saver import DataSaverFactory
from lexicards.interfaces.manager.i_manager import IWordManager


class WordManager(IWordManager):
    """
    Concrete WordManager managing vocabulary words.

    Manages loading, saving, and removing words from CSV files,
    while tracking the current word and meaning.

    Attributes:
        loader_factory (DataRetrieverFactory): Factory for creating data retrievers.
        saver_factory (DataSaverFactory): Factory for creating data savers.
        remover_factory (DataRemoverFactory): Factory for creating data removers.
        source_file (str): CSV file containing all words.
        known_file (str): CSV file to save known words.
        unknown_file (str): CSV file to save unknown words.
        flush_interval (int): Number of marked words before flushing removals to CSV.
        _marked_count (int): Tracks how many words have been marked for removal.
        words (List[List[str]]): List of loaded word pairs.
        current_index (int | None): Index of the current word.
        current_word (str | None): Current word.
        current_meaning (str | None): Meaning of the current word.
        _foreign_language (str | None): Foreign language label from CSV header.
        _native_language (str | None): Native language label from CSV header.
    """

    def __init__(
        self,
        loader_factory: DataRetrieverFactory,
        saver_factory: DataSaverFactory,
        data_remover: DataRemoverFactory,
        source_file: str,
        known_file: str = "known_words.csv",
        unknown_file: str = "unknown_words.csv",
        flush_interval=5,
    ):
        """
        Initialize WordManager.

        Args:
            loader_factory (DataRetrieverFactory): Factory for creating IDataRetriever instances.
            saver_factory (DataSaverFactory): Factory for creating IDataSaver instances.
            data_remover (DataRemoverFactory): Factory for creating IDataRemover instances.
            source_file (str): CSV file containing all words.
            known_file (str): CSV file to save known words.
            unknown_file (str): CSV file to save unknown words.
            flush_interval (int): Number of marked words before flushing to CSV
        """

        self.loader_factory = loader_factory
        self.saver_factory = saver_factory
        self.remover_factory = data_remover

        self.source_file = source_file
        self.known_file = known_file
        self.unknown_file = unknown_file

        self.remover = self.remover_factory.create_data_remover(self.source_file)

        self.flush_interval = flush_interval
        self._marked_count = 0

        self.words: List[List[str]] = self._load_words()
        self.current_index = None
        self.current_word = None
        self.current_meaning = None

        # Language labels
        self._foreign_language: None
        self._native_language: None
        if self.words:
            self._foreign_language = self.words[0][0]
            self._native_language = self.words[0][1]

    # ==========================================================
    # IWordManager Interface
    # ==========================================================

    @property
    def foreign_language(self) -> str:
        return self._foreign_language or "Japanese"

    @property
    def native_language(self) -> str:
        return self._native_language or "English"

    def get_random_word(self) -> Tuple[str, str]:
        """
        Pick a random word from the current list.

        Returns:
            tuple[str, str]: (word, meaning)
        """
        if not self.words or len(self.words[0]) < 2:
            raise ValueError("CSV data must contain at least two columns per row.")

        self.current_index = random.randrange(len(self.words))
        self.current_word = self.words[self.current_index][0]
        self.current_meaning = self.words[self.current_index][1]

        return self.current_word, self.current_meaning

    def mark_as_known(self) -> None:
        """
        Mark the current word as known:
            - Save to known_words.csv
            - Remove from source CSV
            - Remove from in-memory list
        """
        if not self.current_word or not self.current_meaning:
            return

        # Save to known
        saver = self.saver_factory.create_data_saver(self.known_file)
        saver.save_data(self.current_word, self.current_meaning)

        # Mark for removal
        self.remover.mark_for_removal(self.current_word)
        self._marked_count += 1

        if self._marked_count >= self.flush_interval:
            self.remover.flush_async()
            self._marked_count = 0

        # Remove from memory
        if self.current_index is not None:
            self.words.pop(self.current_index)
            self.current_index = None
            self.current_word = None
            self.current_meaning = None

    def mark_as_unknown(self) -> None:
        """
        Mark the current word as unknown:
            - Save to unknown_words.csv
        """
        if not self.current_word or not self.current_meaning:
            return

        saver = self.saver_factory.create_data_saver(self.unknown_file)
        saver.save_data(self.current_word, self.current_meaning)

    # ==========================================================
    # Private Utilities
    # ==========================================================

    def _load_words(self) -> List[List[str]]:
        """
        Load words from the source CSV file.

        Returns:
            list[list[str]]: List of word pairs [word, meaning]

        Raises:
            ValueError: If CSV has fewer than two columns
        """
        retriever = self.loader_factory.create_data_retriever(self.source_file)
        words = retriever.load_data()
        if not words or len(words[0]) < 2:
            raise ValueError("CSV data must contain at least two columns per row.")
        return words
