# -*- coding: utf-8 -*-
# @Time    : 2019-10-12 08:29
# @Author  : yanwallis
# @Site    : 
# @File    : hashdict.py
# @Software: PyCharm

"""
哈希冲突的链式实现,
"""

from structures.array_linked.nodes import Node
from structures.array_linked.arrays import Array
from structures.dicts.abstractdict import AbstractDict, Item


class HashDict(AbstractDict):
    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection=None, capacity=None):
        if capacity is None:
            self._capacity = HashDict.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._items = Array(self._capacity)
        self._foundNode = None  # 引用要调用的节点, 否则返回None
        self._priorNode = None  # 引用定位的节点之前的节点
        self._index = -1  # 引用节点所在链的索引
        AbstractDict.__init__(self, sourceCollection)

    def __contains__(self, item):
        self._index = abs(hash(item))%len(self._items)  # 获取item的哈希索引
        self._priorNode = None
        self._foundNode = self._items[self._index]  # 找到索引位置的值
        while self._foundNode is not None:
            if self._foundNode.data.key == item:
                return True
            else:
                self._priorNode = self._foundNode
                # 找到当前值所在的下一个
                self._foundNode = self._foundNode.next
        return False

    def __iter__(self):
        # 这里的iter记住不是遍历, 因为计算到的索引位置不是按照顺序排列的
        for item in self._items:
            if item:
                yield item.data.key

    def __getitem__(self, key):
        if key in self:
            return self._foundNode.data.value
        else:
            raise KeyError("Missing: "+str(key))

    def __setitem__(self, key, value):
        if key in self:
            self._foundNode.data.value = value
        else:
            self._index = abs(hash(key)) % len(self._items)
            self._items[self._index] = Node(Item(key, value), self._items[self._index])
            self._size += 1

    def pop(self, key):
        if key in self:
            # 分两种情况, 有前一个值, 以及没有前一个值
            if self._priorNode:
                self._priorNode.next = self._foundNode.next
            else:
                # _foundNode有next 以及没有next
                self._items[self._index] = self._priorNode.next
            self._size -= 1
            return self._foundNode.data.value

        else:
            raise KeyError("Missing: "+str(key))


if __name__ == '__main__':
    s = HashDict([("name", "yan"), ("age", 12)])
    print(s)
