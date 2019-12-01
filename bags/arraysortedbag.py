# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 06:52
# @Author  : yanwallis
# @Site    : 
# @File    : arraysortedbag.py
# @Software: PyCharm


from .arraybag import ArrayBag
class ArraySortedBag(ArrayBag):
    """
    有序包， _items必须有序
    """
    def __init__(self, sourceCollection=None):
        ArrayBag.__init__(self, sourceCollection)

    def __contains__(self, item):
        """
        此处实现二分查找法查找， 默认_items 有序
        :param item:
        :return:
        """
        left =0
        right = len(self)-1
        while left <= right:
            middle = (left+right) //2
            if self._items[middle] == item:
                return True
            elif self._items[middle] > item:
                right = middle-1
            else:
                left = middle+1
            return False

    def add(self, item):
        """
        add 比较复杂， 需要保持有序
        :param item:
        :return:
        """
        if self.isEmpty() or self._items[len(self)-1]< item:
            ArrayBag.add(self, item)
        else:
            index = 0
            while item > self._items[index]:
                index += 1
            for i in range(len(self), index, -1):
                self._items[i] = self._items[i-1]
            self._items[index] = item
            self._size += 1

    def __eq__(self, other):
        if self is other:return True
        if type(self) != type(other) or len(self) !=len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True

