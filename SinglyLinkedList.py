class Node :
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, key):
        node = Node(key)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def pop_front(self):
        if self.head is None:
            raise Exception("empty list")
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return self.head.key

    def push_back(self, key):
        node = Node(key)
        node.next = None
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop_back(self):
        if self.head is None:
            raise Exception("empty list")
        if self.head is self.tail:
            k = self.tail
            self.head = self.tail = None
            return k.key
        else:
            k = self.tail
            p = self.head
            while p.next.next is not None:
                p = p.next
            p.next = None
            self.tail = p
            return k.key

    def add_after(self, node, key):
        node2 = Node(key)
        node2.next = node.next
        node.next = node2
        if self.tail is node:
            self.tail = node2
