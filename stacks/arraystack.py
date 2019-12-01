from structures.stacks.abstractstack import AbstractStack
from structures.stacks.arrays import Array


class ArrayStack(AbstractStack):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def push(self, item):
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("The stack is empty")
        item = self._items[len(self) - 1]
        self._size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self._items[len(self) - 1]

    def clear(self):
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)


if __name__ == '__main__':
    s = ArrayStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
