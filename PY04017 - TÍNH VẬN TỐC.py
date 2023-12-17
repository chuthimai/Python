from datetime import timedelta

class Racer:
    def __init__(self):
        self.ho_ten = input()
        self.don_vi = input()
        self.ma = ""
        self.set_ma()
        self.start = timedelta(hours=6)
        h = input().split(":")
        self.end = timedelta(hours=int(h[0]), minutes=int(h[1]))
        self.time = (self.end - self.start).seconds // 60 / 60
        self.v = 120 / self.time

    def set_ma(self):
        for i in self.don_vi.split(): self.ma += i[0]
        for i in self.ho_ten.split(): self.ma += i[0]

    def __repr__(self):
        return self.ma+" "+self.ho_ten+" "+self.don_vi+" "+str(round(self.v))+" Km/h"

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(Racer())
    arr = sorted(arr, key=lambda x: (-x.v))
    for racer in arr: print(racer)



