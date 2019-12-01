import unittest
from sort import (
    bubble_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    radix_sort
)


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

    def test_quick_sort_with_unsorted_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(expected, data)

    def test_quick_sort_with_sorted_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(expected, data)

    def test_quick_sort_with_reversed_data(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(expected, data)

    def test_radix_sort_decimal_with_unsorted_data(self):
        digits = 5
        buckets = 10
        expected = [1, 2, 33, 40, 597, 620, 701, 8909, 9678, 10123]
        data = [2, 40, 620, 8909, 10123, 9678, 701, 597, 33, 1]
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)

    def test_radix_sort_decimal_with_sorted_data(self):
        digits = 5
        buckets = 10
        expected = [1, 2, 33, 40, 597, 620, 701, 8909, 9678, 10123]
        data = [1, 2, 33, 40, 597, 620, 701, 8909, 9678, 10123]
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)

    def test_radix_sort_decimal_with_reversed_data(self):
        digits = 5
        buckets = 10
        expected = [1, 2, 33, 40, 597, 620, 701, 8909, 9678, 10123]
        data = [10123, 9678, 8909, 701, 620, 597, 40, 33, 2, 1]
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)

    def test_radix_sort_binary_with_unsorted_data(self):
        digits = 3
        buckets = 2
        data = [10, 11, 1, 0, 101, 100, 111, 110]
        expected = [0, 1, 10, 11, 100, 101, 110, 111]
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)

    def test_radix_sort_binary_with_sorted_data(self):
        digits = 3
        buckets = 2
        data = [0, 1, 10, 11, 100, 101, 110, 111]
        expected = [0, 1, 10, 11, 100, 101, 110, 111]
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)

    def test_radix_sort_binary_with_reversed_data(self):
        digits = 3
        buckets = 2
        data = [111, 110, 101, 100, 11, 10, 1, 0]
        expected = [0, 1, 10, 11, 100, 101, 110, 111]
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)


if __name__ == "__main__":
    unittest.main()
