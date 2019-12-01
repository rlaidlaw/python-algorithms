import unittest
from search import (
    binary_search
)


class SearchTestCase(unittest.TestCase):

    def test_binary_search(self):
        sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        item = 7
        expected_idx = 6
        actual_idx = binary_search(sorted_data, item)
        self.assertEqual(expected_idx, actual_idx)

    def test_binary_search_not_found(self):
        sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        item = 11
        expected_idx = -1
        actual_idx = binary_search(sorted_data, item)
        self.assertEqual(expected_idx, actual_idx)


if __name__ == "__main__":
    unittest.main()
