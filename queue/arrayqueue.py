"""
pop 的时间复杂度为O(n), 可以考虑循环数组进行优化
"""

from structures.queue.abstractqueue import AbstractQueue
from structures.stacks.arrays import Array


class ArrayQueue(AbstractQueue):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        AbstractQueue.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        """
        pop的时候, 需要"打洞", 时间复杂度为O(n)
        :return:
        :rtype:
        """
        if self.isEmpty():
            raise KeyError("The stack is empty")
        item = self._items[0]
        for i in range(len(self)-1):
            self._items[i] = self._items[i+1]
        self._size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self._items[0]

    def clear(self):
        self._size = 0
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)


if __name__ == '__main__':
    s = ArrayQueue()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    print(s.peek())
    print("=====================")

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
