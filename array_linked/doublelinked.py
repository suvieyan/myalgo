"""
双链表
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DoubleNode(Node):

    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous


class DoubleNodeList():
    def __init__(self):

        self.head = DoubleNode(1)
        self.tail = self.head

    def initialization(self):
        for data in range(2, 6):
            self.tail.next = DoubleNode(data, self.tail)
            self.tail = self.tail.next
        # 尾部访问
        probe = self.tail
        while probe != None:
            print(probe.data)
            probe = probe.previous
        # 头部访问
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next


if __name__ == '__main__':
    l = DoubleNodeList()
    l.initialization()
