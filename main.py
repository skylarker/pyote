from utils.stack.list_stack import ListStack


class Main(object):
    def __init__(self):
        pass

    @staticmethod
    def play():
        list_stack = ListStack(10)
        items = [23, 56, 2, 77, 2, 1]
        for item_ in items:
            list_stack.push(item_)
        list_stack.print()
        print(list_stack.pop())
        print(list_stack.pop())
        print(list_stack.pop())
        print(list_stack.pop())
        print(list_stack.pop())
        print(list_stack.pop())
        print(list_stack.pop())


if __name__ == '__main__':
    main = Main()
    main.play()