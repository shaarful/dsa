class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        pass

    def print_backward(self):
        pass

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_beginning(4)
    dll.insert_at_beginning(6)
    dll.insert_at_beginning(2)

    print(dll)
