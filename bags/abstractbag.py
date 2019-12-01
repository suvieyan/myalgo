# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 07:11
# @Author  : yanwallis
# @Site    : 
# @File    : abstractbag.py
# @Software: PyCharm

from .abstractcollection import AbstractCollection


class AbstractBag(AbstractCollection):
    def __init__(self, sourceCollection=None):
        AbstractCollection.__init__(self, sourceCollection)

    def add(self, other):
        ret = type(self)(other)
        for item in other:
            ret.add(item)
