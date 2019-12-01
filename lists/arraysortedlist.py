"""
pop 的时间复杂度为O(n), 可以考虑循环数组进行优化
"""

from structures.array_linked.arrays import Array
from structures.lists.abstractlist import AbstractList
from structures.lists.arraysortedlistiterator import ArraySortedListIterator


class ArraySortedList(AbstractList):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self._items = Array(ArraySortedList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError()
        return self._items[index]

    def __str__(self):
        return "{" + ", ".join(map(str, self._items)) + "}"

    def __contains__(self, item):
        left = 0
        right = len(self) - 1
        while left <= right:
            middle = (left + right) // 2
            if self._items[middle] == item:
                return True
            elif self._items[middle] > item:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def pop(self, index=None):
        """
        pop的时候, 需要"打洞", 时间复杂度为O(n)
        :return:
        :rtype:
        """
        if index is None:index=len(self)-1
        if index<0 or index>=len(self):
            raise IndexError("List index out of range")

        item = self._items[index]
        for i in range(index, len(self)):
            self._items[i] = self._items[i + 1]
        self._size -= 1
        self.incModCount()
        return item

    def clear(self):
        self._size = 0
        self._items = Array(ArraySortedList.DEFAULT_CAPACITY)

    def add(self, item):
        if self.isEmpty() or self._items[len(self) - 1] < item:
            self._items[len(self)] = item
            self._size += 1
        else:
            index = 0
            while item > self._items[index]:
                index += 1
            for i in range(len(self), index, -1):
                self._items[i] = self._items[i - 1]
            self._items[index] = item
            self._size += 1

    def index(self, item):
        if item not in self._items: raise ValueError(str(item)+" not in sorted list")
        left = 0
        right = len(self) - 1
        while left <= right:
            middle = (left + right) // 2
            if self._items[middle] == item:
                return middle
            elif self._items[middle] > item:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def listIterator(self):
        return ArraySortedListIterator(self)


if __name__ == '__main__':
    s = ArraySortedList(range(8))
    print(s[0])
    print(s[1])
    print(s.index(6))

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print("=====================")
    s.add(12)
    print(s)
    s.add(9)
    print(s)

    print("=====================")

    lyst = ArraySortedList(range(8))
    print("初始", lyst)
    list_iterator = lyst.listIterator()

    for _ in range(2):
        list_iterator.next()
    list_iterator.remove()
    print("remove操作", lyst)

