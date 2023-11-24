import re

def process_name(name: str) -> str:
    name = name.strip()
    name = re.split(r" +", name)
    res = ""
    for n in name:
        res += n.lower()+" "
    return res.title()

sMa = 1
class ThiSinh:
    def __init__(self, ten, diem_thi, dan_toc, khu_vuc):
        global sMa
        self.ma = f"TS%02d" % sMa
        sMa += 1
        self.ten = process_name(ten)
        self.diem_thi = diem_thi
        self.dan_toc = dan_toc
        self.khu_vuc = khu_vuc
        self.diem_ut = self.set_diem_ut()
        self.tong_diem = self.diem_thi + self.diem_ut
        self.trang_thai = self.set_trang_thai()

    def set_diem_ut(self):
        diem_ut = 0
        if self.dan_toc != "Kinh":
            diem_ut += 1.5
        if self.khu_vuc == 1:
            diem_ut += 1.5
        elif self.khu_vuc == 2:
            diem_ut += 1
        return diem_ut

    def set_trang_thai(self):
        if self.tong_diem >= 20.5:
            return "Do"
        else:
            return "Truot"

    def __repr__(self):
        return self.ma+" "+self.ten+f"%.1f"%self.tong_diem+" "+self.trang_thai

if __name__ == "__main__":
    n = int(input())
    all = []
    for i in range(n):
        thi_sinh = ThiSinh(input(), float(input()), input(), int(input()))
        all.append(thi_sinh)
    all.sort(key=lambda x: (-x.tong_diem, x.ma))
    for ts in all:
        print(ts)
