class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        current = 0
        while itr:
            current += 1
            if index == current:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        itr = self.head

        if index == 0:
            self.head = self.head.next
            return

        current_index = 0
        while itr:
            current_index += 1
            if current_index == index:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.append(data)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data

        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        if not self.has_value(data):
            # raise Exception("Data not exist")
            print(f"{data} is not exist")
            return

        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def has_value(self, data):
        itr = self.head

        while itr:
            if itr.data == data:
                return True
            itr = itr.next
        return False

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def print(self):
        if self.head is None:
            print("Link list is empty")
            return
        itr: Node = self.head
        text: str = ""
        while itr:
            text += f"{itr.data}-->"
            itr = itr.next
        print(text)


if __name__ == '__main__':
    linked_list = LinkedList()
    # linked_list.insert_at_beginning(5)
    # linked_list.insert_at_beginning(1)
    # linked_list.insert_at_beginning(7)
    # linked_list.append(8)
    # linked_list.insert_at(2, 11)
    # linked_list.remove_at(4)
    # print(linked_list.get_length())
    linked_list.insert_values([0, 1, 2, 3, 4])
    # linked_list.insert_at(2, 99)
    linked_list.print()

    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    # ll.insert_after_value("banana", "jackfruit")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
