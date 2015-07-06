class StackFullException(Exception):
    def __init__(self):
        super().__init__("Stack is full. Cannot push items into it")
