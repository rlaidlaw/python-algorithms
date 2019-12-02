import unittest
from linked_list import LinkedList, Node


class LinkedListTestCase(unittest.TestCase):

    def test_insert(self):
        expected = 3
        linked_list = LinkedList()
        linked_list.insert(1)
        linked_list.insert(2)
        linked_list.insert(3)
        actual = linked_list.length()
        self.assertEqual(expected, actual)

    def test_append(self):
        expected = 3
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        actual = linked_list.length()
        self.assertEqual(expected, actual)

    def test_delete(self):
        expected = LinkedList()
        expected.append(1)
        expected.append(3)
        actual = LinkedList()
        actual.append(1)
        actual.append(2)
        actual.append(3)
        actual.delete(2)
        self.assertEqual(expected, actual)

    def test_found(self):
        expected = Node(3)
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        actual = linked_list.find(3)
        self.assertEqual(expected, actual)

    def test_not_found(self):
        expected = None
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        actual = linked_list.find(4)
        self.assertEqual(expected, actual)

    def test_length(self):
        expected = 4
        linked_list = LinkedList()
        linked_list.append(3)
        linked_list.append(4)
        linked_list.insert(2)
        linked_list.insert(1)
        actual = linked_list.length()
        self.assertEqual(expected, actual)

    def test_to_list(self):
        expected = [1, 2, 3, 4, 5, 6]
        linked_list = LinkedList()
        linked_list.append(4)
        linked_list.append(5)
        linked_list.append(6)
        linked_list.insert(3)
        linked_list.insert(2)
        linked_list.insert(1)
        actual = linked_list.to_list()
        self.assertEqual(expected, actual)

    def test_list_str(self):
        expected = "[ 1 <-> 2 <-> 3 <-> 4 ]"
        linked_list = LinkedList()
        linked_list.append(3)
        linked_list.append(4)
        linked_list.insert(2)
        linked_list.insert(1)
        actual = str(linked_list)
        self.assertEqual(expected, actual)

    def test_lists_equal(self):
        actual = LinkedList()
        actual.append(1)
        actual.append(2)
        actual.append(3)
        expected = LinkedList()
        expected.insert(3)
        expected.insert(2)
        expected.insert(1)
        self.assertEqual(expected, actual)

    def test_lists_not_equal(self):
        actual = LinkedList()
        actual.append(1)
        actual.append(2)
        actual.append(3)
        expected = LinkedList()
        expected.insert(3)
        expected.insert(2)
        expected.insert(1)
        self.assertEqual(expected, actual)

    def test_node_str(self):
        expected = "1"
        node = Node(1)
        actual = str(node)
        self.assertEqual(expected, actual)

    def test_nodes_equal(self):
        expected = Node(1)
        actual = Node(1)
        self.assertEqual(expected, actual)

    def test_nodes_not_equal(self):
        expected = Node(1)
        actual = Node(2)
        self.assertNotEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
