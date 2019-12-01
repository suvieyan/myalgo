"""
pop 的时间复杂度为O(n), 可以考虑循环数组进行优化
"""

from structures.array_linked.arrays import Array
from structures.lists.abstractlist import AbstractList
from structures.lists.arraylistiterator import ArrayListIterator


class ArrayList(AbstractList):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
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

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self):
            raise IndexError("List index out of range")
        self._items[index] = value

    def __str__(self):
        return "{" + ", ".join(map(str, self._items)) + "}"

    def insert(self, index, value):
        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)
        if index <= len(self):
            for j in range(len(self), index, -1):
                self._items[j] = self._items[j-1]
        self._items[index] = value
        self._size += 1
        self.incModCount()

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

    def listIterator(self):
        return ArrayListIterator(self)


if __name__ == '__main__':
    s = ArrayList()
    s.insert(1, "a")
    s.insert(1, "b")
    s.insert(1, "c")
    s.insert(1, "d")
    print(s[0])
    print(s[1])
    print("=====================")
    s[1] = "asd"

    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    list_iterator = s.listIterator()
    while list_iterator.has_next():
        print(list_iterator.next())
    print("=====================")

    while list_iterator.has_previous():
        print(list_iterator.previous())

    print("=====================")

    lyst = ArrayList(range(8))
    print("初始", lyst)
    list_iterator = lyst.listIterator()

    for _ in range(2):
        list_iterator.next()
    list_iterator.insert("asd")
    print("insert 操作", lyst)
    for _ in range(2):
        list_iterator.next()
    list_iterator.remove()
    print("remove操作", lyst)

    for _ in range(2):
        list_iterator.next()
    list_iterator.replace("hello")
    print("replace操作", lyst)
"""
初始 {0, 1, 2, 3, 4, 5, 6, 7, None, None}
insert 操作 {0, asd, 1, 2, 3, 4, 5, 6, 7, None}
remove操作 {0, asd, 1, 3, 4, 5, 6, 7, None, None}
replace操作 {0, asd, 1, 3, hello, 5, 6, 7, None, None}
"""
