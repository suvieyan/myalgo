"""
优先级队列, 按照优先级进行排序
"""

from structures.array_linked.nodes import Node
from structures.queue.linkedqueue import LinkedQueue


class LinkedPriorityQueue(LinkedQueue):

    def __init__(self, sourceCollection=None):
        LinkedQueue.__init__(self, sourceCollection)

    def add(self, item):
        if self.isEmpty() or item >= self.rear.data:
            LinkedQueue.add(self, item)
        else:
            probe = self.front
            while item >= probe.data:  # 比较优先级的值, 值越大, 优先级越低, 重写比较方法,
                trailer = probe
                probe = probe.next
            new_node = Node(item, probe)
            if probe == self.front:
                self.front = new_node
            else:
                trailer.next = new_node
        self._size +=1


if __name__ == '__main__':
    q = LinkedPriorityQueue()
    from structures.queue.comparable import Comparable
    q.add(Comparable("a", 2))
    q.add(Comparable("f", 4))
    q.add(Comparable("e", 8))
    q.add(Comparable("d", 5))
    q.add(Comparable("a", 6))
    q.add(Comparable("b", 1))
    q.add(Comparable("c", 3))
    print(q.peek())
    print(q.pop())
    print(q.pop())

