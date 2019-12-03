class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        node = Node(data)
        head = self.head
        if head is not None:
            node.set_next(head)
            head.set_prev(node)
        self.head = node

    def append(self, data):
        node = Node(data)
        current = self.head
        if current is None:
            self.head = node
        else:
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(node)
            node.set_prev(current)

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is not None:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def find(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return current

    def length(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.get_next()
        return count

    def to_list(self):
        data = []
        current = self.head
        while current is not None:
            data.append(current.get_data())
            current = current.get_next()
        return data

    def __str__(self):
        return "[ " + " <-> ".join([str(d) for d in self.to_list()]) + " ]"

    def __eq__(self, other):
        return self.to_list() == other.to_list()

    def __ne__(self, other):
        return self.to_list() != other.to_list()


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __str__(self):
        return str(self.data)
