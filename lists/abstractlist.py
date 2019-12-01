# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 07:11
# @Author  : yanwallis
# @Site    : 
# @File    : abstractstack.py
# @Software: PyCharm

from structures.abstractcollection import AbstractCollection


class AbstractList(AbstractCollection):
    def __init__(self, sourceCollection=None):
        self._modCount = 0
        AbstractCollection.__init__(self, sourceCollection)

    def getModCount(self):
        return self._modCount

    def incModCount(self):
        self._modCount += 1

    def index(self, item):
        position = 0
        for i in self:
            if i == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError(str(item)+"not in list")

    def remove(self, item):
        position = self.index(item)
        self.pop(position)

    def add(self, item):
        self.insert(len(self), item)


