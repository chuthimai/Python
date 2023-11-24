from decimal import ROUND_HALF_UP, Decimal

sMa = 1
class HocSinh:
    def __init__(self):
        self.ma = "HS" + (f"%02d" % sMa)
        self.ten = input()
        self.diem = [Decimal(x) for x in input().split()]
        self.diemTB = self.tinh_diemTB().quantize(Decimal('0.1'), ROUND_HALF_UP)
        self.xepLoai = self.xet_xep_loai()

    def tinh_diemTB(self):
        x = 2 * self.diem[0] + 2 * self.diem[1]
        for i in range(2, 10):
            x += self.diem[i]
        return x/Decimal(12)

    def xet_xep_loai(self):
        if self.diemTB >= 9: return "XUAT SAC"
        elif self.diemTB >= 8: return "GIOI"
        elif self.diemTB >= 7: return "KHA"
        elif self.diemTB >= 5: return "TB"
        else: return "YEU"

    def __repr__(self):
        return self.ma+" "+self.ten+" "+str(self.diemTB)+" "+self.xepLoai


if __name__ == "__main__":
    n = int(input())
    ds_hoc_sinh = []
    for i in range(n):
        ds_hoc_sinh.append(HocSinh())
        sMa += 1
    ds_hoc_sinh = sorted(ds_hoc_sinh, key=lambda x: (-x.diemTB, x.ma))
    for i in range(n):
        print(ds_hoc_sinh[i])