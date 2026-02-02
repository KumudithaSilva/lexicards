import unittest
from unittest.mock import MagicMock

from lexicards.data.data_remover import DataRemoverFactory
from lexicards.data.data_retriever import DataRetrieverFactory
from lexicards.data.data_saver import DataSaverFactory
from lexicards.interfaces.data.i_data_retriever import IDataRetriever
from lexicards.manager.word_manager import WordManager


class TestWordManager(unittest.TestCase):
    def setUp(self):

        self.mock_loader_factory = MagicMock(spec=DataRetrieverFactory)
        self.mock_retriever = MagicMock(spec=IDataRetriever)
        self.mock_loader_factory.create_data_retriever.return_value = (
            self.mock_retriever
        )

        self.mock_saver_factory = MagicMock(spec=DataSaverFactory)
        self.mock_saver = MagicMock()
        self.mock_saver_factory.create_data_saver.return_value = self.mock_saver

        self.mock_remover_factory = MagicMock(spec=DataRemoverFactory)
        self.mock_remover = MagicMock()
        self.mock_remover_factory.create_data_remover.return_value = self.mock_remover

        self.mock_retriever.load_data.return_value = [
            ["Japanese", "English"],
            ["川", "River"],
            ["山", "Mountain"],
        ]

        self.manager = WordManager(
            loader_factory=self.mock_loader_factory,
            saver_factory=self.mock_saver_factory,
            data_remover=self.mock_remover_factory,
            source_file="mock.csv",
        )

    def test_get_random_word(self):
        current_word, current_meaning = self.manager.get_random_word()
        self.assertIn([current_word, current_meaning], self.manager.words)

    def test_mark_as_known(self):
        self.manager.current_word = "川"
        self.manager.current_meaning = "River"

        self.manager.mark_as_known()
        self.mock_remover.mark_for_removal.assert_called_once_with(
            self.manager.current_word
        )

    def test_mark_as_unknown_called(self):
        self.manager.current_word = "川"
        self.manager.current_meaning = "River"
        self.manager.unknown_file = "mock_unknown.csv"

        self.manager.mark_as_unknown()

        self.manager.saver_factory.create_data_saver(self.manager.unknown_file)
        self.mock_saver.save_data.assert_called_once_with("川", "River")

    def test_properties(self):
        self.assertEqual(self.manager.foreign_language, "Japanese")
        self.assertEqual(self.manager.native_language, "English")

    def test_load_words(self):
        words = self.manager.words  # Already loaded in __init__
        self.assertEqual(words[1], ["川", "River"])
        self.assertEqual(words[2], ["山", "Mountain"])
        self.mock_loader_factory.create_data_retriever.assert_called_once_with(
            "mock.csv"
        )
        self.mock_retriever.load_data.assert_called_once()


if __name__ == "__main__":
    unittest.main()
