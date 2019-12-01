# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 22:52
# @Author  : yanwallis
# @Site    : 
# @File    : arraydict.py
# @Software: PyCharm
from structures.dicts.abstractdict import AbstractDict, Item


class ArrayDict(AbstractDict):
    def __init__(self,sourceCollection=None):
        self._items = list()
        AbstractDict.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = 0
        while cursor<len(self):
            yield self._items[cursor].key
            cursor += 1

    def __getitem__(self, key):
        index = self._index(key)
        if index == -1:
            raise KeyError("Missing: "+str(key))
        return self._items[index].value

    def __setitem__(self, key, value):
        index = self._index(key)
        if index == -1:
            self._items.append(Item(key, value))
            self._size += 1
        else:
            self._items[index].value = value

    def pop(self, key):
        index = self._index(key)

        if index == -1:
            raise KeyError("Missing: "+str(key))
        self._size -= 1
        return self._items.pop(index).value

    def _index(self, key):
        index = 0
        for item in self._items:
            if item.key == key:
                return index
            index += 1
        return -1

if __name__ == '__main__':
    d = ArrayDict()
    d["name"] = "yan"
    d["age"] = "12"
    print(d)
