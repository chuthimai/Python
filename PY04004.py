# PY04004 - LỚP PHÂN SỐ - 2

import math

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self.compact()
    def compact(self):
        ucln = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator//ucln
        self.denominator = self.denominator//ucln
    def convert(self, n:int):
        self.numerator = self.numerator * n
        self.denominator = self.denominator * n
    def __add__(self, other):
        ucln = math.gcd(self.denominator, other.denominator)

        self.convert(other.denominator//ucln)
        other.convert(self.denominator//other.denominator)
        return Fraction(self.numerator + other.numerator, self.denominator)
    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)

a, b, c, d = [int(x) for x in input().split()]
f1 = Fraction(a, b)
f2 = Fraction(c, d)
f3 = f1 + f2
f3.compact()
print(f3)
