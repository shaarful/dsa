from collections import deque


# s = []
# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')
#
# stack = deque()
# stack.append('https://www.cnn.com/')
# stack.append('https://www.cnn.com/world')
# stack.append('https://www.cnn.com/india')
# stack.append('https://www.cnn.com/china')


# print(stack)
# print(stack[-1])
# print(stack)


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def reverse_string(self, s: str):
        ns = deque(s)
        rs = ''
        while len(ns) > 0:
            rs += ns.pop()
        return rs


def is_balanced(s: str) -> bool:
    stack = Stack()
    for c in s:
        stack.push(c)
        print(stack.peek())

    return False


is_balanced("({a+b})")
is_balanced("))((a+b}{")
is_balanced("((a+b))")
is_balanced("))")
is_balanced("[a+b]*(x+2y)*{gg+kk}")

a = Stack()
print(a.reverse_string("We will conquere COVID-19"))
