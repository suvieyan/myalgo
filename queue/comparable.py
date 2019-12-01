class Comparable:
    def __init__(self, data, priority=1):
        self._data = data
        self._priority = priority

    def __str__(self):
        return self._data

    def __eq__(self, other):
        if self is other:return True
        if type(self) != type(other): return False
        return self._priority == other._priority

    def __le__(self, other):
        return self._priority <= other._priority

    def __lt__(self, other):
        return self._priority < other._priority

    @property
    def data(self):
        return self._data

    @property
    def priority(self):
        return self._priority
