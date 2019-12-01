from arrays import Array


class Grid(object):
    def __init__(self, rows, columns, value=None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, value)

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        result = ""
        for row in range(self.height):
            for col in range(self.width):
                result += str(self._data[row][col]) + " "
            result += "\n"
        return result

    @property
    def height(self):
        return len(self._data)

    @property
    def width(self):
        return len(self._data[0])


if __name__ == '__main__':
    g = Grid(3, 4, 1)
    print(g)
    print(g[1][1])
