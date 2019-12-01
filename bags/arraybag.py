from .arrays import Array
from .abstractbag import AbstractBag

class ArrayBag(AbstractBag):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        AbstractBag.__init__(self, sourceCollection)

    def __str__(self):
        return "{" + ", ".join(map(str, self._items)) + "}"

    def __iter__(self):
        cursor = 0
        while cursor<len(self):
            yield self._items[cursor]
            cursor += 1

    def clear(self):
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1

    def remove(self, item):
        index = 0
        for target_item in self:
            if target_item == item:
                break
            index += 1
        for i in range(index, len(self)-1):
            self._items[i] = self._items[i+1]
        self._size -= 1
