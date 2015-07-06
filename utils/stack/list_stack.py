from exceptions.stack.empty_stack_exception import EmptyStackException
from exceptions.stack.stack_full_exception import StackFullException


class ListStack(Exception):
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []  # stack is a list

    def pop(self):
        if self.is_empty():
            raise EmptyStackException()
        else:
            return self.stack.pop()

    def push(self, item):
        if self.is_full():
            raise StackFullException()
        else:
            self.stack.append(item)

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        if self.get_size() < self.max_size:
            return False
        else:
            return True

    def peek(self):
        temp = self.stack.pop()
        self.push(temp)
        return temp

    def flush(self):
        self.stack = []

    def print(self):
        print(self.stack)

    def pretty_print(self):
        pass

    def get_size(self):
        return len(self.stack)