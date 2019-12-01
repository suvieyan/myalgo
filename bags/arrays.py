"""
存在问题:
当动态进行扩容的时候, 实际的self被变更的问题
"""

DEFAULT_CAPACITY = 5


class Array:

    def __init__(self, capacity, value=None):
        self._items = []

        for _ in range(capacity):
            self._items.append(value)

        self.capacity = capacity

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
        self._items[key] = value

    @staticmethod
    def _increase(a):
        if a.capacity == len(a):
            temp = Array(len(a) + 1)
            for i in range(a.capacity):
                temp[i] = a[i]
            a = temp
        return a

    def _decrease(self):
        if self.capacity <= len(self) // 4 and len(a) >= DEFAULT_CAPACITY * 2:
            temp = Array(len(self) // 2)
            for i in range(self.capacity):
                temp[i] = self[i]
            self = temp


class MyList(Array):
    def insert(self, index, item):
        _self = self._increase(self)
        for i in range(self.capacity, index, -1):
            _self[i] = self[i-1]
        _self[index] = item
        self = _self

    def delete(self, index):
        for i in range(index, self.capacity):
            self[i] = self[i+1]
        self._decrease()


if __name__ == '__main__':

    a = MyList(5)

    print(len(a))

    print(a)

    for i in range(len(a)):
        a[i] = i + 1

    l = a.insert(3, 6)
    print(11111111, a)
    print(l)



