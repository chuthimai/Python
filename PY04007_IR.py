# PY04007 - LỚP MATRIX - 1

import numpy as np


class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = []

    def T(self):
        m = Matrix(self.column, self.row)
        res = np.array(self.matrix).T
        m.matrix = list(res)
        return m

    def dot(self, other):
        if self.column == other.row:
            m = Matrix(self.row, other.column)
            res = np.array(self.matrix).dot(np.array(other.matrix))
            m.matrix = list(res)
            return m
        else:
            return Matrix(0, 0)

    def __repr__(self):
        res = ""
        for i in range(self.row):
            for j in range(self.column):
                res += str(self.matrix[i][j]) + " "
            res += "\n"
        return res


def one_time():
    row, column = [int(x) for x in input().split()]
    m = Matrix(row, column)
    for i in range(row):
        l = [int(x) for x in input().split()[:column]]
        m.matrix.append(l)
    print(m.dot(m.T()), end="")


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        one_time()




