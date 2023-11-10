# PY04019 - TUYỂN NHÂN VIÊN

sMa = 1
class NhanVien:
    def __init__(self, ten, lt, th):
        global sMa
        self.ma = f"TS0{sMa}"
        sMa += 1
        self.ten = ten
        self.diem_tb = (self.diem(lt) + self.diem(th))/2
        self.loai = self.xet_loai()

    def xet_loai(self):
        if self.diem_tb < 5: return "TRUOT"
        elif self.diem_tb < 8: return "CAN NHAC"
        elif self.diem_tb < 9.5: return "DAT"
        else: return "XUAT SAC"

    def diem(self, d):
        if d > 10:
            return d/10
        else:
            return d

    def __repr__(self):
        return self.ma+" "+self.ten+" "+f"%.2f" % self.diem_tb+" "+self.loai

if __name__ == "__main__":
    n = int(input())
    all_nv = []
    for i in range(n):
        all_nv.append(NhanVien(input(), float(input()), float(input())))

    all_nv.sort(key=lambda x: x.diem_tb, reverse=True)
    for nv in all_nv: print(nv)


