from structures.array_linked.nodes import Node
from structures.queue.abstractqueue import AbstractQueue


class LinkedQueue(AbstractQueue):

    def __init__(self, sourceCollection=None):
        AbstractQueue.__init__(self, sourceCollection)
        self.front = None
        self.rear = None

    def __iter__(self):
        def visit_nodes(node):
            if node:
                visit_nodes(node.next)
                temp_list.append(node.data)

        temp_list = list()
        visit_nodes(self.front)
        return iter(temp_list)

    def add(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("The stack is empty")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self.front.data


if __name__ == '__main__':
    s = LinkedQueue()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    print(s.peek())
    print(s.pop())
    print(s.pop())
