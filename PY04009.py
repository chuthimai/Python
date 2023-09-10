# PY04009 - LỚP SỐ PHỨC

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def __add__(self, other):
        return Complex(self.real+other.real, self.img+other.img)
    def __mul__(self, other):
        real = self.real*other.real - self.img*other.img
        img = self.real*other.img + self.img*other.real
        return Complex(real, img)
    def __repr__(self):
        if self.img > 0:
            return f"{self.real} + {self.img}i"
        elif self.img < 0:
            return f"{self.real} - {abs(self.img)}i"
        else:
            return f"{self.real}"

times = int(input())
for i in range(times):
    a, b, c, d = [int(x) for x in input().split()]
    complex1 = Complex(a, b)
    complex2 = Complex(c, d)
    sum = complex1+complex2
    print(f"{sum * complex1}, {sum * sum}")



