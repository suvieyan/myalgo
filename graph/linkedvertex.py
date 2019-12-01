# -*- coding: utf-8 -*-
# @Time    : 2019-10-12 08:30
# @Author  : yanwallis
# @Site    : 
# @File    : linkedvertex.py
# @Software: PyCharm

from structures.graph.linkededge import LinkedEdge


class LinkedVertex:
    def __init__(self, label):
        self._label = label
        self._mark = False
        self._edgeList = list()

    def __str__(self):pass

    def __eq__(self, other):
        if self is other:return True
        if type(self) != type(other):return False
        return self._label == other._label

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
    def getLabel(self):
        """
        返回顶点的标签
        :return:
        :rtype:
        """

    def setLabel(self, label, g):
        g._vertices.pop(label, None)
        g._vertices[label] = self
        self._label = label

    def assEdgeTo(self, toVertex, weight):
        """
        从当前点到toVertex 添加一条有权重的边
        :param toVertex:
        :type toVertex:
        :param weight:
        :type weight:
        :return:
        :rtype:
        """

    def removeEdgeTo(self, toVertex):
        edge = LinkedEdge(self, toVertex)
        if edge in self._edgeList:
            self._edgeList.remove(edge)
            return True
        return False

    def incidentEdges(self):
        """
        返回顶点想关边上的一个迭代器
        :return:
        :rtype:
        """

    def neighnoringVertices(self):
        vertices = list()
        for edge in self._edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)
