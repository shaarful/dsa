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
    open_first = 0
    open_second = 0
    open_third = 0
    for c in s:
        #     stack.push(c)
        # b = stack.is_empty()
        # print(b)
        # while not stack.is_empty():
        #     a = stack.peek()
        a = c
        if a == '(':
            open_first += 1
        elif a == ')':
            open_first -= 1
        elif a == '{':
            open_second += 1
        elif a == '}':
            open_second -= 1
        elif a == '[':
            open_third += 1
        elif a == ']':
            open_third -= 1

        if open_first < 0 or open_second < 0 or open_third < 0:
            return False
    if open_first != 0 or open_second != 0 or open_third != 0:
        return False
    # print(stack.peek())

    return True


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

a = Stack()
print(a.reverse_string("We will conquere COVID-19"))
