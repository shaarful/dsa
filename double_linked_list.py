class NodeIterator:
    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node:
            self.node = self.node.next
            return self.node
        raise StopIteration


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def iterator(self):
        itr = self.head
        while itr:
            yield itr
            itr = itr.next

    def iterator_prev(self):
        itr = self.get_last_node()
        while itr:
            yield itr
            itr = itr.prev

    def get_last_node(self):
        if self.head is None:
            return None
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_forward(self):
        text = ''
        for n in self.iterator():
            text += str(n.data)
            if n.next is not None:
                text += "-->"
        print(text)

    def print_backward(self):
        text = ''
        for n in self.iterator_prev():
            text += str(n.data)
            if n.prev is not None:
                text += "-->"
        print(text)

    def get_length(self):
        count = 0
        for node in NodeIterator(self.head):
            count += 1
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def append(self, data):
        last_node = self.get_last_node()
        node = Node(data, None, last_node)
        if self.head is None:
            self.head = node
            return
        last_node.next = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        for n in self.iterator():
            if index - 1 == count:
                # n=1 n.next = 3
                # node = 2
                node = Node(data, n.next, n)
                n.next = node
                if node.next:
                    node.next.prev = node
                break
                # n.prev = n.prev
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        for n in self.iterator():
            if count == index - 1:
                # n=1 n.next = 2
                n.next = n.next.next
                if n.next:
                    n.next.prev = n
                break
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)


if __name__ == '__main__':
    dll = DoublyLinkedList()
    # dll.insert_at_beginning(4)
    # dll.insert_at_beginning(6)
    # dll.insert_at_beginning(2)
    dll.append(1)
    dll.append(3)
    dll.append(4)
    dll.insert_at(1, 2)
    dll.print_forward()
    dll.print_backward()
    dll.remove_at(3)
    dll.insert_values([4, 5, 6])
    dll.print_forward()
    dll.print_backward()
