import unittest
from sort import bubble_sort


class SortTestCase(unittest.TestCase):

    def test_bubble_sort_with_random_data(self):
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = bubble_sort(data)
        self.assertEqual(expected, actual)

    def test_bubble_sort_with_sorted_data(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = bubble_sort(data)
        self.assertEqual(expected, actual)

    def test_bubble_sort_with_reversed_data(self):
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = bubble_sort(data)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
