"""
队列的接口
"""


class QueueInterface:
    def __init__(self, sourceCollection):pass
    def isEmpty(self): return True
    def __len__(self): return 0
    def __iter__(self): return True
    def __contains__(self, item):pass
    def __str__(self): return ""
    def __add__(self, other): return None
    def __eq__(self, other): return False
    def clear(self): pass
    def peek(self): pass
    def add(self): pass
    def pop(self): pass

