"""
循环链表
插入删除, 不用考虑头部尾部
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:

    def __init__(self):
        self.head = Node(None, None)  # 哑头节点
        self.head.next = self.head

    def initialization(self):
        head = self.head
        for count in range(1, 6):
            head = Node(count, head)
        self.head.next = head

        # probe = self.head
        # while probe.next != self.head:
        #     probe = probe.next
        #     print(probe.data)

    def __iter__(self):
        """
        for循环
        :return:
        :rtype:
        """
        probe = self.head
        while probe.next != self.head:
            probe = probe.next
            yield probe.data

    def __len__(self):
        count = 0
        probe = self.head
        while probe.next != self.head:
            probe = probe.next
            count += 1
        return count


if __name__ == '__main__':
    l = CircularLinkedList()
    l.initialization()
    print("----------------------")
    for i in l:
        print(i)

    print(len(l))
