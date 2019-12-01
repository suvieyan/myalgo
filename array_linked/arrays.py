"""
存在问题:
当动态进行扩容的时候, 实际的self被变更的问题
"""

DEFAULT_CAPACITY = 5


class Array:

    def __init__(self, capacity, value=None):
        self._items = list()
        self._capacity = capacity

        for _ in range(self._capacity):
            self._items.append(value)

    def __len__(self):
        """
        获取长度
        :return:
        :rtype:
        """
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        """
        for 循环遍历
        :return:
        :rtype:
        """
        return iter(self._items)

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        print(111111111, key, len())
        self._items[key] = value

    def isEmpty(self):
        return len(self) == 0

    # def _add(self, item):
    #     self[0] = item

    def insert(self, index, item):
        if len(self) >= self._capacity:
            raise IndexError("Array is full")
        if index>=len(self): index =len(self)
        if index<0: index = 0
        if index == len(self):
            self._items.append(item)
        else:
            print(1111111111, index, item, len(self))

            for i in range(len(self), index, -1):
                self[i] = self[i-1]
            self[index] = item

    def remove(self, index):
        if index<0 or index>=len(self): return False
        for i in range(index, self._capacity):
            self[i] = self[i+1]


    # @staticmethod
    # def _increase(a):
    #     if a.capacity == len(a):
    #         temp = Array(len(a) + 1)
    #         for i in range(a.capacity):
    #             temp[i] = a[i]
    #         a = temp
    #     return a
    #
    # def _decrease(self):
    #     if self.capacity <= len(self) // 4 and len(a) >= DEFAULT_CAPACITY * 2:
    #         temp = Array(len(self) // 2)
    #         for i in range(self.capacity):
    #             temp[i] = self[i]
    #         self = temp


if __name__ == '__main__':

    a = Array(5)
    print(a)

    a.insert(3, 6)
    a.insert(3, 1)
    a.insert(3, 2)
    a.insert(3, 3)
    a.insert(3, 4)
    print(11111111, a)

