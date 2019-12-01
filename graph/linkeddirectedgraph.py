# -*- coding: utf-8 -*-
# @Time    : 2019-10-12 08:32
# @Author  : yanwallis
# @Site    : 
# @File    : linkeddirectedgraph.py
# @Software: PyCharm

from structures.abstractcollection import AbstractCollection
from structures.graph.linkedvertex import LinkedVertex


class LinkedDirectedGraph(AbstractCollection):
    def __init__(self, sourceCollection):
        self._edgeCount = 0
        self._vertices = dict()
        AbstractCollection.__init__(self, sourceCollection)

    def __str__(self):pass

    # 清除标记/大小

    def clear(self):
        """
        从图中删除所有顶点
        :return:
        :rtype:
        """
    def clearEdgeMarks(self):
        """
        清除所有边标记
        :return:
        :rtype:
        """
    def clearVertexMarks(self):
        """
        清除所有顶点标记
        :return:
        :rtype:
        """
    def sizeEdges(self):
        """
        返回图中边的数目
        :return:
        :rtype:
        """
    def sizeVertices(self):
        """
        返回图中顶点的数目
        :return:
        :rtype:
        """

    # 顶点相关
    def containsVertex(self, label):
        """
        是否包含指定标签的顶点
        :param label:
        :type label:
        :return:
        :rtype:
        """
    def addVertex(self, label):
        """
        添加指定标签的顶点
        :param label:
        :type label:
        :return:
        :rtype:
        """
        self._vertices[label] = LinkedVertex(label)
        self._size += 1

    def removeVertex(self, label):
        """
        删除指定标签的顶点, 没有返回None, 有返回该顶点
        :param label:
        :type label:
        :return:
        :rtype:
        """
        removeVertex = self._vertices.pop(label, None)
        if not removeVertex:
            return False
        for vertex in self.vertiecs():
            if vertex.removeEdgeTo(removeVertex):
                self._edgeCount -= 1
        for edge in removeVertex.incidentEdges():
            self._edgeCount -= 1
        self._size -= 1
        return True

    def getVertex(self, label):
        """获取指定标签的顶点, 没有返回None"""
        pass

    # 边相关

    def containsEdge(self, fromLabel, toLabel):
        """从图中获取从fromLabel到toLabel的边, 有返回TRUE, 没有False"""
    def addEdge(self, fromLabel, toLabel, weight):
        """
        指定两个顶点之间,添加一条边
        :param fromLabel:
        :type fromLabel:
        :param toLabel:
        :type toLabel:
        :param weight:
        :type weight:
        :return:
        :rtype:
        """
        fromVertex = self.addVertex(fromLabel)
        toVertex = self.addVertex(toLabel)
        fromVertex.addEdgeTo(toVertex, weight)
        self._edgeCount += 1

    def getEdge(self, fromLabel, toLabel):
        """获取两个顶点之间的边"""
        fromVertex =self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)

    def removeEdge(self, fromLabel, toLabel):
        """删除两个顶点之间的边"""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        edgeremoveflag = fromVertex.removeEdgeTo(toVertex)
        if edgeremoveflag:
            self._edgeCount -= 1
        return edgeremoveflag

    # 迭代器想关
    def edges(self):
        """返回边的迭代器"""
        result = set()
        for vertex in self.vertices():
            edges = vertex.incidentEdges()
            result = result.union(set(edges))
        return iter(result)

    def vertices(self):
        """图中顶点的迭代器"""
        return

    def incidentEdges(self, label):
        """返回标记的顶点想关的边上的迭代器"""
    def neighoringVertices(self, label):
        """返回标记的顶点相邻的顶点上的迭代器"""