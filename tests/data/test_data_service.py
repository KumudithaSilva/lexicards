import unittest
from unittest.mock import MagicMock

from lexicards.interfaces.data.i_data_retriever import IDataRetriever
from lexicards.interfaces.data.i_data_saver import IDataSaver


class TestDataServices(unittest.TestCase):
    def test_data_retriever_load_data(self):
        mock_retriever = MagicMock(spec=IDataRetriever)
        mock_retriever.load_data.return_value = [["こんにちは", "Hello"], ["川", "River"]]

        data = mock_retriever.load_data()

        self.assertIsInstance(data, list)
        self.assertEqual(data[0], ["こんにちは", "Hello"])

    def test_data_saver_save_data(self):
        mock_saver = MagicMock(spec=IDataSaver)
        mock_saver.save_data("川", "River")

        mock_saver.save_data.assert_called_once_with("川", "River")


if __name__ == "__main__":
    unittest.main()
