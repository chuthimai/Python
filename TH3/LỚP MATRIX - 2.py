
class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = None

    def T(self):
        res = Matrix(self.m, self.n)
        m = []
        for i in range(self.m):
            l = []
            for j in range(self.n):
                l.append(self.matrix[j][i])
            m.append(l)
        res.matrix = m
        return res

    def mulT(self):
        other = self.T()

        res = Matrix(self.n, other.m)
        m = []
        for i in range(self.n):
            l = []
            for j in range(other.m):
                a = 0
                for k in range(self.n):
                    a += self.matrix[i][k]*other.matrix[k][j]
                l.append(a)
            m.append(l)
        res.matrix = m
        return res


def one_time():
    n, m = map(int, input().split()[:2])
    arr = []
    for i in range(n):
        l = [int(x) for x in input().split()[:m]]
        arr.append(l)
    matrix = Matrix(n, m)
    matrix.matrix = arr
    res = matrix.mulT()
    for x in res.matrix:
        print(*x)

if __name__ == "__main__":
    n = int(input().split()[0])
    for i in range(n):
        one_time()

