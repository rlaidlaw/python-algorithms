import unittest
from sort import bubble_sort


class SortTestCase(unittest.TestCase):

    def test_bubble_sort(self):
        data = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = bubble_sort(data)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
