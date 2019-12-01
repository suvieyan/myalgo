# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 07:19
# @Author  : yanwallis
# @Site    : 
# @File    : abstractcollection.py
# @Software: PyCharm


class AbstractCollection:
    def __init__(self, sourceCollection=None):
        self._size = 0  # 记录逻辑大小
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """
        需要重新定义
        :return:
        """
        pass

    def __eq__(self, other):
        """
        比较两个集合
        :param other:
        :return:
        """
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False

        other_iter = iter(other)
        for item in self:
            if item != next(other_iter):
                return False
        return True

    def __len__(self):
        return self._size

    def __add__(self, other):
        ret = type(self)(other)
        for item in other:
            ret.add(item)

    def add(self, item):
        raise NotImplementedError
