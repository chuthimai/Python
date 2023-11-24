import datetime

maTT = 1
class TheLoai:
    def __init__(self, ten):
        global maTT
        self.ma = f"TL%03d" % maTT
        maTT += 1
        self.ten = ten

maP = 1
class Phim:
    def __init__(self, ma_tt, ngay, ten_phim, so_tap):
        global maP
        self.ma = f"P%03d" % maP
        maP += 1
        self.ma_tt = ma_tt
        self.the_loai = None
        self.set_the_loai()
        self.ngay = ngay
        d = ngay.split("/")
        self.date = datetime.datetime(day=int(d[0]), month=int(d[1]), year=int(d[2]))
        self.ten_phim = ten_phim
        self.so_tap = so_tap

    def set_the_loai(self):
        global list_tt
        for tt in list_tt:
            if self.ma_tt == tt.ma:
                self.the_loai = tt.ten
                break

    def __repr__(self):
        return self.ma+" "+self.the_loai+" "+self.ngay+" "+self.ten_phim+" "+str(self.so_tap)


if __name__ == '__main__':
    n, m = map(int, input().split())
    list_tt = []
    for i in range(n):
        tt = TheLoai(input())
        list_tt.append(tt)
    list_phim = []
    for i in range(m):
        phim = Phim(input(), input(), input(), int(input()))
        list_phim.append(phim)
    list_phim.sort(key=lambda x: (x.date, x.ten_phim, -x.so_tap))
    for phim in list_phim:
        print(phim)


