"""
二叉搜索树
特点: 左子树的节点小于给定节点, 右子树节点大于给定节点
"""

from structures.abstractcollection import AbstractCollection
from structures.stacks.linkedstack import LinkedStack
from structures.lists.linkedlist import LinkedList
from structures.queue.linkedqueue import LinkedQueue
from structures.trees.bstnode import BSTNode


class LinkedBST(AbstractCollection):
    def __init__(self, sourceCollection):
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    def __str__(self):
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level+1)
                s += "| "*level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._root, 0)

    def __iter__(self):
        """
        前序遍历
        :return:
        :rtype:
        """
        s = LinkedStack()
        if self._root is not None:
            s.push(self._root)
        while not s.isEmpty():
            node = s.pop()
            yield node.data
            s.push(node.left)
            s.push(node.right)

    def find(self, item):
        """
        查找二叉搜索树
        :param item:
        :type item:
        :return:
        :rtype:
        """

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    def inorder(self):
        """
        中序遍历
        :return:
        :rtype:
        """
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """
        后序遍历
        :return:
        :rtype:
        """
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self._root)
        return iter(lyst)

    def levelorder(self):
        """
        层遍历
        :return:
        :rtype:
        """
        lyst = list()
        q = LinkedQueue()
        if self._root is not None:
            q.add(self._root)
        def recurse():
            while not q.isEmpty():
                item = q.pop()
                lyst.append(item.data)
                if item.left is not None:
                    q.add(item.left)
                if item.right is not None:
                    q.add(item.right)
        recurse()
        return iter(lyst)

    def add(self, item):
        def recurse(node):
            if item < node.data:
                # 左边
                if node.left is None:
                    node.left = BSTNode(item, parent=node)
                else:
                    recurse(node.left)
            else:
                if node.right is None:
                    node.right = BSTNode(item, parent=node)
                else:
                    recurse(node.right)
        if self.isEmpty():
            self._root = BSTNode(item)
        else:
            recurse(self._root)

        self._size += 1

    def remove(self, item):
        """
        1.保存根节点
        2.找到要删除的节点/其父节点/其父节点对该节点的引用
        3.如果该节点有左节点和右节点, 则左节点的最大值代替该节点, 左子树删除该节点的值
        4.否则, 父节点对该节点的引用设置为该节点的自己的节点
        5.根节点重新设置为保存的引用
        6.大小减1, 返回该项
        :param item:
        :type item:
        :return:
        :rtype:
        """
        # 通过搜索得到需要删除的节点
        node = self.find(item)
        # 父节点为空，又不是根节点，已经不在树上，不用再删除
        if node.parent is None and node != self._root:
            raise ValueError("item not in the tree")

        self._del(node)

    def _del(self, node):
        """
        删除
        所删除的节点N存在以下情况：
        1. 没有子节点：直接删除N的父节点指针
        2. 有一个子节点：将N父节点指针指向N的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        :param node:
        :return:
        """
        # 1
        if node.left is None and node.right is None:
            # 情况1和2，根节点和普通节点的处理方式不同
            if node == self._root:
                self._root = None
            else:
                if node.data < node.parent.data:
                    node.parent.left = None
                else:
                    node.parent.right = None

                node.parent = None
        # 2
        elif node.left is None and node.right is not None:
            if node == self._root:
                self._root = node.right
                self._root.parent = None
                node.right = None
            else:
                if node.data < node.parent.data:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

                node.right.parent = node.parent
                node.parent = None
                node.right = None
        elif node.left is not None and node.right is None:
            if node == self._root:
                self._root = node.left
                self._root.parent = None
                node.left = None
            else:
                if node.data < node.parent.data:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

                node.left.parent = node.parent
                node.parent = None
                node.left = None
        # 3
        else:
            min_node = node.right
            # 找到右子树的最小值节点
            if min_node.left:
                min_node = min_node.left

            if node.data != min_node.data:
                node.data = min_node.data
                self._del(min_node)
            # 右子树的最小值节点与被删除节点的值相等，再次删除原节点
            else:
                self._del(min_node)
                self._del(node)


if __name__ == '__main__':
    t = LinkedBST(range(10))
    print(t.find(3).data)
    print(list(t.inorder()))
    print(list(t.postorder()))
    print(list(t.levelorder()))

    t = LinkedBST([3,4,6,1,2,9,0])
    print(t.find(3).data)
    print(list(t.inorder()))
    print(list(t.postorder()))
    print(list(t.levelorder()))

    t.remove(3)
    print(t)

