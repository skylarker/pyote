class ListStack(Exception):
    def __init__(self, max_size=100000):
        self.max_size = max_size
        self.data = []

    def pop(self):
        pass

    def push(self, item):
        pass

    def is_empty(self):
        pass

    def is_full(self):
        pass

    def print(self):
        pass

    def pretty_print(self):
        pass

    def get_size(self):
        pass

if __name__ == '__main__':
    stack = ListStack()
    stack.push(5)