# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 22:37
# @Author  : yanwallis
# @Site    : 
# @File    : abstractdict.py
# @Software: PyCharm
from structures.abstractcollection import AbstractCollection


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) +":"+str(self.value)

    def __eq__(self, other):
        if type(self) != type(other):return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other):return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other):return False
        return self.key <= other.key


class AbstractDict(AbstractCollection):
    def __init__(self, sourceCollection):
        AbstractCollection.__init__(self)
        if sourceCollection:
            for key, value in sourceCollection:
                self[key] = value

    def __str__(self):
        return "{" + ", ".join(map(str, self.items())) + "}"

    def __add__(self, other):
        result = type(self)(map(lambda item:(item.key, item.value), self.items()))
        for key in other:
            result[key] = other[key]
        return result

    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for key in self:
            if not key in other:
                return False
        return True

    def keys(self):
        return iter(self)

    def values(self):
        return iter(map(lambda key:self[key], self))

    def items(self):
        return iter(map(lambda key:Item(key, self[key]), self))

