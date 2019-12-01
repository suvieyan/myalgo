class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeList:

    def __init__(self):
        head = None
        for count in range(1, 6):
            head = Node(count, head)
        self.head = head

    def __iter__(self):
        """
        for循环
        :return:
        :rtype:
        """
        """
        遍历链表
        :return:
        :rtype:
        """
        probe = self.head
        while probe != None:
            yield probe.data
            probe = probe.next

    def __len__(self):
        count = 0
        probe = self.head
        while probe != None:
            probe = probe.next
            count += 1
        return count

    def search(self, data):
        """
        查找值是否在链表
        :param data:
        :type data:
        :return:
        :rtype:
        """
        probe = self.head
        while probe != None and probe.data != data:
            probe = probe.next
        if probe != None:
            return True
        else:
            return False

    def find(self, index):
        """
        根据位置查找值
        :param index:
        :type index:
        :return:
        :rtype:
        """
        if index < 0 or index > len(self):
            raise IndexError
        probe = self.head
        while index:
            probe = probe.next
            index -= 1
        return probe.data

    def replace_data(self, old_data, new_data):
        """
        从链表找到值并替换
        :param old_data:
        :type old_data:
        :param new_data:
        :type new_data:
        :return:
        :rtype:
        """
        probe = self.head
        while probe != None and probe.data != old_data:
            probe = probe.next
        if probe != None:
            probe.data = new_data
            return True
        else:
            return False

    def replace_index(self, index, new_data):
        """
        替换某个位置的值
        :param index:
        :type index:
        :param new_data:
        :type new_data:
        :return:
        :rtype:
        """
        if index < 0 or index > len(self):
            raise IndexError
        probe = self.head
        while index:
            probe = probe.next
            index -= 1
        probe.data = new_data

    def insert_left(self, item):
        """
        链表左侧插入值
        :param item:
        :type item:
        :return:
        :rtype:
        """
        self.head = Node(item, self.head)

    def insert_right(self, item):
        """
        链表右侧追加
        :param item:
        :type item:
        :return:
        :rtype:
        """
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = new_node

    def insert(self, index, data):
        """
        任意位置插入值
        :param index:
        :type index:
        :param data:
        :type data:
        :return:
        :rtype:
        """
        if index < 0 or index > len(self):
            raise IndexError
        if self.head is None or index<=0:
            self.head = Node(data, self.head)
        else:
            probe = self.head
            while index>1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = Node(data, probe.next)

    def pop_left(self):
        """
        左边删除
        :return:
        :rtype:
        """
        if self.head is None:
            raise IndexError
        item = self.head.data
        self.head = self.head.next
        return item

    def pop_right(self):
        """
        右边删除
        :return:
        :rtype:
        """
        if self.head is None:
            raise IndexError
        else:
            probe = self.head
            while probe.next.next != None:
                probe = probe.next
            item = probe.next.data
            probe.next = None
            return item

    def pop(self, index):
        """
        任意位置删除
        :param index:
        :type index:
        :return:
        :rtype:
        """
        if index < 0 or index > len(self):
            raise IndexError
        if index<=0 or self.head.next is None:
            item = self.head.data
            self.head = self.head.next
            return item
        elif index>= len(self):
            self.pop_right()
        else:
            probe = self.head
            while index>1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            item = probe.next.data
            probe.next = probe.next.next
            return item


if __name__ == '__main__':
    node_list = NodeList()
    # print(len(node_list))
    # ret = node_list.search(6)
    # print(ret)
    #
    # ret = node_list.find(2)
    # print(ret)

    node_list.insert_left(8)
    # print(node_list.head.data)

    node_list.insert_right(9)
    print(list(node_list))
    # print(node_list.head.data)
    print(node_list.pop_left())
    print(node_list.pop_right())

    print(node_list.find(3))

    node_list.insert(3, "a")
    print(list(node_list))

    node_list.pop(3)
    print(list(node_list))
