# PY04003 - LỚP PHÂN SỐ - 1
import math

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.__numerator = numerator
        self.__denominator = denominator
        self.compact()
    def compact(self):
        ucln = math.gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator//ucln
        self.__denominator = self.__denominator//ucln
    def __repr__(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

a, b = [int(x) for x in input().split()]
fraction = Fraction(a, b)
print(fraction)
