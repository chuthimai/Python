# PY04002 - LỚP RECTANGLE

class Rectangle:
    def __init__(self, a: int, b: int, color: str):
        self.__a = a
        self.__b = b
        self.__color = color
    def perimeter(self):
        return (self.__a + self.__b)*2
    def area(self):
        return self.__a * self.__b
    def color(self):
        return self.__color.capitalize()

    def __repr__(self):
        if self.__a > 0 and self.__b > 0:
            return '{} {} {}'.format(self.perimeter(), self.area(), self.color())
        else:
            return "INVALID"


arr = input().split()[:3]
r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
print(r)