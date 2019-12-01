import unittest
from random import sample
from sort import (
    bubble_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    radix_sort
)


class BubbleSortTestCase(unittest.TestCase):

    def test_bubble_sort_with_unsorted_data_even(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        bubble_sort(data)
        self.assertEqual(expected, data)

    def test_bubble_sort_with_unsorted_data_odd(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        data = [2, 11, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        bubble_sort(data)
        self.assertEqual(expected, data)

    def test_bubble_sort_with_empty_input(self):
        expected = []
        data = []
        bubble_sort(data)
        self.assertEqual(expected, data)

    def test_bubble_sort_with_small_input(self):
        expected = [1]
        data = [1]
        bubble_sort(data)
        self.assertEqual(expected, data)

    def test_bubble_sort_with_large_input(self):
        expected = list(range(1, 1001))
        data = sample(expected, len(expected))
        bubble_sort(data)
        self.assertEqual(expected, data)

    def test_bubble_sort_with_negative_data(self):
        expected = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        data = [-3, -5, -9, -6, -1, -10, -4, -7, -2, -8]
        bubble_sort(data)
        self.assertEqual(expected, data)

    def test_bubble_sort_with_mixed_sign_data(self):
        expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        data = [3, -5, 0, -2, -1, 1, -3, 4, 5, -4, 2]
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


class SelectionSortTestCase(unittest.TestCase):

    def test_selection_sort_with_unsorted_data_even(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        selection_sort(data)
        self.assertEqual(expected, data)

    def test_selection_sort_with_unsorted_data_odd(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        data = [2, 11, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        selection_sort(data)
        self.assertEqual(expected, data)

    def test_selection_sort_with_empty_input(self):
        expected = []
        data = []
        selection_sort(data)
        self.assertEqual(expected, data)

    def test_selection_sort_with_small_input(self):
        expected = [1]
        data = [1]
        selection_sort(data)
        self.assertEqual(expected, data)

    def test_selection_sort_with_large_input(self):
        expected = list(range(1, 1001))
        data = sample(expected, len(expected))
        selection_sort(data)
        self.assertEqual(expected, data)

    def test_selection_sort_with_negative_data(self):
        expected = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        data = [-3, -5, -9, -6, -1, -10, -4, -7, -2, -8]
        selection_sort(data)
        self.assertEqual(expected, data)

    def test_selection_sort_with_mixed_sign_data(self):
        expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        data = [3, -5, 0, -2, -1, 1, -3, 4, 5, -4, 2]
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


class MergeSortTestCase(unittest.TestCase):

    def test_merge_sort_with_unsorted_data_even(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        merge_sort(data)
        self.assertEqual(expected, data)

    def test_merge_sort_with_unsorted_data_odd(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        data = [2, 11, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        merge_sort(data)
        self.assertEqual(expected, data)

    def test_merge_sort_with_empty_input(self):
        expected = []
        data = []
        merge_sort(data)
        self.assertEqual(expected, data)

    def test_merge_sort_with_small_input(self):
        expected = [1]
        data = [1]
        merge_sort(data)
        self.assertEqual(expected, data)

    def test_merge_sort_with_large_input(self):
        expected = list(range(1, 1001))
        data = sample(expected, len(expected))
        merge_sort(data)
        self.assertEqual(expected, data)

    def test_merge_sort_with_negative_data(self):
        expected = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        data = [-3, -5, -9, -6, -1, -10, -4, -7, -2, -8]
        merge_sort(data)
        self.assertEqual(expected, data)

    def test_merge_sort_with_mixed_sign_data(self):
        expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        data = [3, -5, 0, -2, -1, 1, -3, 4, 5, -4, 2]
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


class QuickSortTestCase(unittest.TestCase):

    def test_quick_sort_with_unsorted_data_even(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(expected, data)

    def test_quick_sort_with_unsorted_data_odd(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        data = [2, 11, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(expected, data)

    def test_quick_sort_with_empty_input(self):
        expected = []
        data = []
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(expected, data)

    def test_quick_sort_with_small_input(self):
        expected = [1]
        data = [1]
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(expected, data)

    def test_quick_sort_with_large_input(self):
        expected = list(range(1, 1001))
        data = sample(expected, len(expected))
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(expected, data)

    def test_quick_sort_with_negative_data(self):
        expected = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        data = [-3, -5, -9, -6, -1, -10, -4, -7, -2, -8]
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(expected, data)

    def test_quick_sort_with_mixed_sign_data(self):
        expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        data = [3, -5, 0, -2, -1, 1, -3, 4, 5, -4, 2]
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


class RadixSortTestCase(unittest.TestCase):

    def test_radix_sort_decimal_with_unsorted_data_even(self):
        digits = 5
        buckets = 10
        expected = [1, 2, 33, 40, 597, 620, 701, 8909, 9678, 10123]
        data = [2, 40, 620, 8909, 10123, 9678, 701, 597, 33, 1]
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)

    def test_radix_sort_decimal_with_unsorted_data_odd(self):
        digits = 5
        buckets = 10
        expected = [1, 2, 33, 40, 597, 620, 701, 8909, 9678, 10123, 98550]
        data = [2, 98550, 40, 620, 8909, 10123, 9678, 701, 597, 33, 1]
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)

    def test_radix_sort_decimal_with_empty_input(self):
        digits = 5
        buckets = 10
        expected = []
        data = []
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)

    def test_radix_sort_decimal_with_small_input(self):
        digits = 5
        buckets = 10
        expected = [1]
        data = [1]
        radix_sort(data, buckets, digits)
        self.assertEqual(expected, data)

    def test_radix_sort_decimal_with_large_input(self):
        digits = 5
        buckets = 10
        expected = list(range(1, 10001))
        data = sample(expected, len(expected))
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
