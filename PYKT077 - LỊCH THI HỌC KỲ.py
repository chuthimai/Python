import datetime
from datetime import timedelta

class MonHoc:
    def __init__(self):
        self.ma = input()
        self.tenMH = input()

class LichThi:
    def __init__(self):
        global ma_ca_thi
        self.info = input().split()
        self.ma = f"T%03d" % ma_ca_thi
        ma_ca_thi += 1
        self.ma_mon = self.info[0]
        date = self.info[1].split("/")
        time = self.info[2].split(":")
        self.nhom = self.info[3]
        self.time = timedelta(hours=int(time[0]), minutes=int(time[1]))
        self.date = datetime.date(
            day=int(date[0]),
            month=int(date[1]),
            year=int(date[2])
        )

    def ten_mon(self):
        global arr_mon_thi
        for mon_thi in arr_mon_thi:
            if mon_thi.ma == self.ma_mon:
                return mon_thi.tenMH
        return

    def __repr__(self):
        return self.ma+" "+self.ma_mon+" "+self.ten_mon()+" "+self.info[1]+" "+self.info[2]+" "+self.nhom


if __name__ == '__main__':
    ma_ca_thi = 1
    arr_lich_thi = []
    arr_mon_thi = []
    so_mon_thi, so_lich_thi = map(int, input().split())
    for i in range(so_mon_thi):
        arr_mon_thi.append(MonHoc())
    for i in range(so_lich_thi):
        arr_lich_thi.append(LichThi())

    arr_lich_thi.sort(key=lambda x: (x.date, x.time, x.ma_mon))
    for lich_thi in arr_lich_thi:
        print(lich_thi)


