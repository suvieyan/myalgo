# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 22:19
# @Author  : yanwallis
# @Site    : 
# @File    : abstractset.py
# @Software: PyCharm


class AbstractSet:
    def __init__(self):pass

    def __or__(self, other):
        return self + other

    def __and__(self, other):
        intersection = type(self)()
        for item in self:
            if item in other:
                intersection.add(item)
        return intersection

    def __sub__(self, other):
        difference = type(self)()
        for item in self:
            if item not in other:
                difference.add(item)
        return difference

    def issubset(self, other):
        for item in self:
            if item not in other:
                return False
        return True
