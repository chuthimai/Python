# PY04005 - LỚP TRIANGLE - 1
import math

class Point:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
    def distance(self, other):
        x = self.__x - other.__x
        y = self.__y - other.__y
        return math.sqrt(x*x + y*y)

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.e1 = p1.distance(p2)
        self.e2 = p1.distance(p3)
        self.e3 = p2.distance(p3)
    def perimeter(self):
        return self.e1 + self.e2 + self.e3
    def isTraingle(self):
        isTrue = True
        edges = [self.e1, self.e2, self.e3]
        edges.sort()
        if edges[0] == 0:
            isTrue = False
        if edges[0] + edges[1] <= edges[2]:
            isTrue = False
        if edges[2] - edges[1] >= edges[0] or edges[2] - edges[0] >= edges[1]:
            isTrue = False
        return isTrue

    def __repr__(self):
        if self.isTraingle():
            return "%.3f" % self.perimeter()
        else:
            return "INVALID"
# Note: input in the same time
a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    triangle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    print(triangle)
    i += 6

