import unittest
from sort import bubble_sort, selection_sort, merge_sort


class SortTestCase(unittest.TestCase):

    def test_bubble_sort_with_unsorted_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        bubble_sort(data)
        self.assertEqual(expected, data)

    def test_bubble_sort_with_sorted_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bubble_sort(data)
        self.assertEqual(expected, data)

    def test_bubble_sort_with_reversed_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        bubble_sort(data)
        self.assertEqual(expected, data)

    def test_selection_sort_with_unsorted_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        selection_sort(data)
        self.assertEqual(expected, data)

    def test_selection_sort_with_sorted_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        selection_sort(data)
        self.assertEqual(expected, data)

    def test_selection_sort_with_reversed_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        selection_sort(data)
        self.assertEqual(expected, data)

    def test_merge_sort_with_unsorted_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        merge_sort(data)
        self.assertEqual(expected, data)

    def test_merge_sort_with_sorted_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        merge_sort(data)
        self.assertEqual(expected, data)

    def test_merge_sort_with_reversed_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        merge_sort(data)
        self.assertEqual(expected, data)


if __name__ == "__main__":
    unittest.main()
