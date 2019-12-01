# -*- coding: utf-8 -*-
# @Time    : 2019-10-12 08:31
# @Author  : yanwallis
# @Site    : 
# @File    : linkededge.py
# @Software: PyCharm

class LinkedEdge:
    def __init__(self, fromVertex, toVertex, weight=None):
        self._vertex1 = fromVertex
        self._vertex2 = toVertex
        self._weight = weight
        self._mark = False

    def __eq__(self, other):
        if self is other:return True
        if type(self) != type(other):return False
        return self._vertex1 == other._vertex1 and self._vertex2 == other._vertex2 and self._weight == other._weight

    def __str__(self):pass

    def getToVertex(self):
        """
        返回该边的目标顶点
        :return:
        :rtype:
        """
        pass

    def getOtherVertex(self, vertex):
        """
        返回该边的另一个顶点
        :param vertex:
        :type vertex:
        :return:
        :rtype:
        """
        pass
    def getWeight(self):
        """
        返回边的权重
        :return:
        :rtype:
        """
    def setWeight(self, weight):
        """
        重新指定边的权重
        :param weight:
        :type weight:
        :return:
        :rtype:
        """

    def setMark(self):
        """
        标记该边
        :return:
        :rtype:
        """

    def clearMark(self):
        """
        取消边的标记
        :return:
        :rtype:
        """
    def isMarked(self):
        """
        标记了返回TRUE, 否则返回False
        :return:
        :rtype:
        """
