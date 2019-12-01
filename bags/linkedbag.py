from .nodes import Node
from .abstractbag import AbstractBag

class LinkedBag(AbstractBag):

    def __init__(self, sourceCollection=None):
        self._items = None
        AbstractBag.__init__(self, sourceCollection)

    def __str__(self):
        return "{" + ", ".join(map(str, self._items)) + "}"

    def __iter__(self):
        cursor = self._items
        while cursor:
            yield cursor.data
            cursor = cursor.next

    def clear(self):
        self._size = 0
        self._items = None

    def add(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        probe = self._items
        trailer = None
        for target_item in self:
            if target_item == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        self._size -= 1


