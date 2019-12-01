# -*- coding: utf-8 -*-
# @Time    : 2019-10-12 08:27
# @Author  : yanwallis
# @Site    : 
# @File    : hashset.py
# @Software: PyCharm



"""
TODO 这里实现不对
哈希冲突的链式实现,
这里需要优化下, 索引加了, 但是其实值是没有添加的
"""

from structures.array_linked.nodes import Node
from structures.array_linked.arrays import Array
from structures.sets.abstractset import AbstractSet
from structures.abstractcollection import AbstractCollection


class HashSet(AbstractCollection, AbstractSet):
    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection=None, capacity=None):
        if capacity is None:
            self._capacity = HashSet.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._items = Array(self._capacity)
        self._foundNode = None  # 引用要调用的节点, 否则返回None
        self._priorNode = None  # 引用定位的节点之前的节点
        self._index = -1  # 引用节点所在链的索引
        AbstractCollection.__init__(self, sourceCollection)

    def __contains__(self, item):
        self._index = abs(hash(item))%len(self._items)  # 获取item的哈希索引
        self._priorNode = None
        self._foundNode = self._items[self._index]  # 找到索引位置的值
        while self._foundNode is not None:
            if self._foundNode.data == item:
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
                yield item.data

    def __str__(self):

        return "{" + ", ".join(map(str, self)) + "}"

    def clear(self):
        self._size = 0
        self._items = Array(self._capacity)

    def add(self, item):
        if item not in self:
            self._items[self._index] = Node(item, self._items[self._index])
            self._size += 1

    def remove(self, item):
        if item in self:
            while self._foundNode is not None:
                if self._foundNode.data == item:
                    # 分两种情况, 有前一个值, 以及没有前一个值
                    if self._priorNode:
                        self._priorNode.next = self._foundNode.next
                        self._foundNode.next = None
                    else:
                        # _foundNode有next 以及没有next
                        if self._foundNode.next is not None:
                            self._items[self._index] = self._foundNode.next
                            self._foundNode.next = None
                        else:
                            self._items[self._index] = Node(None)
                    self._size -= 1
                    break
                else:
                    self._priorNode = self._foundNode
                    # 找到当前值所在的下一个
                    self._foundNode = self._foundNode.next


if __name__ == '__main__':
    s = HashSet(range(4))
    print(s)
    s.remove(1)
    print(s)