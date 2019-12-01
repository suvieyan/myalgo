"""
堆中的每一个节点的值都必须大于或者等于其子树的每一个节点的值
完全二叉树当中, 索引和节点之间的关系, 假设节点索引为i
父节点:(i-1)/2
左兄弟节点: i-1
右兄弟节点: i+1
左孩子节点: i*2+1
右孩子节点: i*2+2
"""

from structures.abstractcollection import AbstractCollection


class ArrayHeap(AbstractCollection):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        # self._items = Array(ArrayHeap.DEFAULT_CAPACITY)
        self._heap = []
        AbstractCollection.__init__(self, sourceCollection)

    def __str__(self):
        return "{" + ", ".join(map(str, self._heap)) + "}"

    # def __iter__(self):
    #     cursor = 0
    #     while cursor < len(self):
    #         yield self._items[cursor]
    #         cursor += 1

    def add(self, item):
        self._size += 1
        self._heap.append(item)
        curPos = len(self._heap) - 1
        while curPos > 0:
            parent = (curPos - 1) // 2
            parent_item = self._heap[parent]
            if parent_item <= item:
                break
            else:
                # 新节点的值小于父节点的值, 新元素沿着堆向上走
                print("=============")
                print("item", item)
                print("curPos", curPos)
                print("parent", parent)
                print("=============")

                self._heap[curPos] = self._heap[parent]
                self._heap[parent] = item
                curPos = parent

    def pop(self):
        if self.isEmpty():
            raise ValueError("Heap is empty")
        self._size -= 1
        top_item = self._heap[0]
        bottom_item = self._heap.pop(len(self._heap) -1)
        if len(self._heap) == 0:
            return bottom_item

        self._heap[0] = bottom_item
        last_index = len(self._heap) -1
        curPos = 0
        while True:
            left_child = 2*curPos+1
            right_child = 2*curPos+2
            if left_child>last_index:
                break
            if right_child >last_index:
                max_child = left_child
            else:
                left_item = self._heap[left_child]
                right_item = self._heap[right_child]
                if left_item <right_item:
                    max_child = left_child
                else:
                    max_child = right_child
            max_item = self._heap[max_child]
            if bottom_item<= max_item:
                break
            else:
                self._heap[curPos] = self._heap[max_child]
                self._heap[max_child] = bottom_item
                curPos = max_child
        return top_item


    def peek(self):
        pass


if __name__ == '__main__':
    h = ArrayHeap(range(12, 20))
    print(h)
    h.add(12)
    h.add(9)
    h.add(11)
    h.add(8)
    print(h)
    h.pop()
    print(h)
    h.pop()
    print(h)

"""
{8, 11, 9, 13, 12, 14, 18, 19, 15, 16, 12, 17}
{9, 11, 14, 13, 12, 17, 18, 19, 15, 16, 12}
{11, 12, 14, 13, 12, 17, 18, 19, 15, 16}
"""