import unittest
from fibonacci import (
    fibonacci_basic,
    fibonacci_memo,
    fibonacci_dynamic
)


class FibonacciTestCase(unittest.TestCase):

    def test_fibonacci_basic(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        actual = [fibonacci_basic(n) for n in range(len(expected))]
        self.assertEqual(expected, actual)

    def test_fibonacci_memo(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        actual = [fibonacci_memo(n) for n in range(len(expected))]
        self.assertEqual(expected, actual)

    def test_fibonacci_dynamic(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        actual = [fibonacci_dynamic(n) for n in range(len(expected))]
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
