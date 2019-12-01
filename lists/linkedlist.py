from structures.lists.abstractlist import AbstractList
from structures.lists.linkedlistiterator import LinkedListIterator
from structures.array_linked.doublelinked import DoubleNode


class LinkedList(AbstractList):

    def __init__(self, sourceCollection=None):
        self._head = DoubleNode(None)  # head是哑头节点
        self._head.previous = self._head.next = self._head
        AbstractList.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = self._head.next
        while cursor != self._head:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return "{" + ", ".join(map(str, [item for item in self])) + "}"

    def _getNode(self, index):
        # 头结点
        if index == len(self):
            return self._head
        # 尾节点
        if index == len(self) - 1:
            return self._head.previous
        probe = self._head.next
        while index > 0:
            probe = probe.next
            index -= 1
        return probe

    def __setitem__(self, key, value):
        if key < 0 or key >= len(self):
            raise IndexError("List index out of range")
        self._getNode(key).data = value

    def __getitem__(self, index):
        return self._getNode(index).data

    def insert(self, index, value):
        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)
        node = self._getNode(index)
        new_node = DoubleNode(value, previous=node.previous, next=node)
        node.previous.next = new_node
        node.previous = new_node

        self._size += 1
        self.incModCount()

    def pop(self, index=None):
        if index is None: index = len(self) - 1
        if index < 0 or index >= len(self):
            raise IndexError("List index out of range")
        the_node = self._getNode(index)
        the_node.previous.next = the_node.next
        the_node.next.previous = the_node.previous

        self._size -= 1
        self.incModCount()
        return the_node.data

    def listIterator(self):
        return LinkedListIterator(self)


if __name__ == '__main__':
    s = LinkedList()
    s.insert(1, "a")
    s.insert(1, "b")
    s.insert(1, "c")
    s.insert(1, "d")
    print(s[0])
    print(s[1])
    print("=====================")

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

    print("=====================")

    lyst = LinkedList(range(8))
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
初始 {0, 1, 2, 3, 4, 5, 6, 7}
insert 操作 {0, asd, 1, 2, 3, 4, 5, 6, 7}
remove操作 {0, asd, 1, 3, 4, 5, 6, 7}
replace操作 {0, asd, 1, 3, hello, 5, 6, 7}
"""
