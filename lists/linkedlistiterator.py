"""
由于列表实现索引了, 所以此方法可以实现,的按时效率低
"""


class LinkedListIterator:
    def __init__(self, backingStore):
        """
        :param backingStore:
        :type backingStore:
        """
        self._backingStore = backingStore
        self._modCount = backingStore.getModCount()  # 这个变量保证backingStore 在这个过程当中没有干扰的操作
        self.first()

    def first(self):
        """
        将游标移动到第一项之前
        self._cursor: 需要维护的游标
        self._lastItemPos: 最后一次next或者previous的位置, insert和remove和replace之后,未定义, 设置为-1
        :return:
        :rtype:
        """
        self._cursor = 0
        self._lastItemPos = -1

    def last(self):
        """
        将游标移动到最后一项之后
        :return:
        :rtype:
        """
        self._cursor = len(self._backingStore)
        self._lastItemPos = -1

    def has_next(self):
        """
        如果游标之后有项, 返回TRUE,
        如果游标未定义, 或者位于最后一项之后, 返回False
        :return:
        :rtype:
        """
        return self._cursor < len(self._backingStore)

    def has_previous(self):
        """
        如果游标之前有项, 返回TRUE,
        如果游标未定义, 或者位于第一项之前, 返回False
        :return:
        :rtype:
        """
        return self._cursor > 0

    def next(self):
        """
        返回下一项, 并将游标向右移动一个位置
        :return:
        :rtype:
        """
        if not self.has_next():
            raise ValueError("No next item in the list Iterator")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        self._lastItemPos = self._cursor
        self._cursor += 1
        return self._backingStore[self._lastItemPos]

    def previous(self):
        """
        返回前一项, 并将游标向左移动一个位置
        :return:
        :rtype:
        """
        if not self.has_previous():
            raise ValueError("No previous item in the list Iterator")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        self._cursor -= 1
        self._lastItemPos = self._cursor
        return self._backingStore[self._lastItemPos]

    def insert(self, item):
        """
        如果定义了_lastItemPos 从其后插入, 否则, 从列表尾部插入, _lastItemPos被重置为-1
        此操作修改_modCount 的值
        :param item:
        :type item:
        :return:
        :rtype:
        """
        if self._lastItemPos == -1:
            self._backingStore.add(item)
        else:
            self._backingStore.insert(self._lastItemPos, item)
        self._modCount += 1
        self._lastItemPos = -1

    def remove(self):
        """
        删除最近一次next或者previous操作返回的项,  且列表没有被修改, _lastItemPos 被重置为-1
        1._lastItemPos 有效
        2._modCount 等于self._backingStore.getModCount()
        3.此操作修改_modCount 的值
        :return:
        :rtype:
        """
        if self._lastItemPos == -1:
            raise AttributeError("The current position is undefined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        self._backingStore.pop(self._lastItemPos)
        if self._lastItemPos < self._cursor:
            self._cursor -= 1
        self._modCount += 1
        self._lastItemPos = -1

    def replace(self, item):
        """
        替代最近一次next或者previous操作返回的项, 且列表没有被修改, _lastItemPos 被重置为-1
        1._lastItemPos 有效
        2._modCount 等于self._backingStore.getModCount()
        3.此操作不修改_modCount 的值
        :param item:
        :type item:
        :return:
        :rtype:
        """
        if self._lastItemPos == -1:
            raise AttributeError("The current position is undefined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        self._backingStore[self._lastItemPos] = item
        self._lastItemPos = -1
