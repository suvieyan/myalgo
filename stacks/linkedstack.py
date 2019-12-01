from structures.stacks.nodes import Node
from structures.stacks.abstractstack import AbstractStack


class LinkedStack(AbstractStack):

    def __init__(self, sourceCollection= None):
        self._items = None
        AbstractStack.__init__(self, sourceCollection)

    def __iter__(self):
        def visit_nodes(node):
            if node:
                visit_nodes(node.next)
                temp_list.append(node.data)
        temp_list = list()
        visit_nodes(self._items)
        return iter(temp_list)

    def push(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("The stack is empty")
        item = self._items.data
        self._items = self._items.next
        self._size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self._items.data

if __name__ == '__main__':
    s = LinkedStack()
    s.push(3)
    s.push(4)
    print(s.peek())
    print(s.pop())
    print(s.pop())
