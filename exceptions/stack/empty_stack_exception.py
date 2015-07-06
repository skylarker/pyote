class EmptyStackException(Exception):
    def __init__(self):
        super().__init__("Stack is empty. Cannot pop an empty stack.")