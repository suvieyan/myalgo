# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 22:24
# @Author  : yanwallis
# @Site    : 
# @File    : arrayset.py
# @Software: PyCharm
from structures.sets.abstractset import AbstractSet
from structures.bags.arraybag import ArrayBag


class ArraySet(ArrayBag, AbstractSet):
    def __init__(self, sourceCollection):
        ArrayBag.__init__(self, sourceCollection)

    def __str__(self):
        return "{" + ", ".join(map(str, self._items)) + "}"

    def add(self, item):
        if not item in self:
            ArrayBag.add(self, item)


if __name__ == '__main__':
    s = ArraySet(range(4))
    print(s)

    s1 = ArraySet([3,4])
    print(s1)
    print(s.issubset(s1))