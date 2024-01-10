import threading
import time
from collections import deque
from multiprocessing import Process

price = []

price.insert(0, 232)
price.insert(0, 123)
price.insert(0, 523)


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def front(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
oq = Queue()


def order_process():
    for order in orders:
        time.sleep(0.5)
        oq.enqueue(order)
        print(f"{order} has been placed")


def serve_process():
    time.sleep(1)
    while oq.size() != 0:
        time.sleep(2)
        print(f"{oq.dequeue()} has been served")


def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    # pq = Queue()
    #
    # pq.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15 apr, 11.01 AM',
    #     'price': 131.10
    # })
    # pq.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15 apr, 11.02 AM',
    #     'price': 132
    # })
    # pq.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15 apr, 11.03 AM',
    #     'price': 135
    # })
    #
    # print(pq.dequeue())

    # p1 = threading.Thread(target=order_process)
    # p2 = threading.Thread(target=serve_process)
    #
    # p1.start()
    # p2.start()

    produce_binary_numbers(10)
