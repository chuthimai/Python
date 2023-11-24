sMa = 1

class GiaoVien:
    def __init__(self, ten, maXT, diem_tin, diem_cm):
        global sMa
        self.ma = f"GV%02d" % sMa
        sMa += 1
        self.ten = ten
        self.maXT = maXT
        self.diem_tin = diem_tin
        self.diem_cm = diem_cm
        self.chuyen_mon = self.set_chuyen_mon()
        self.tong_diem = self.set_tong_diem()
        self.trang_thai = self.set_trang_thai()

    def set_chuyen_mon(self):
        if self.maXT[0] == 'A': return "TOAN"
        elif self.maXT[0] == 'B': return "LY"
        elif self.maXT[0] == 'C': return "HOA"

    def set_tong_diem(self):
        diem_ut = 0
        if self.maXT[1] == '1': diem_ut = 2
        elif self.maXT[1] == '2': diem_ut = 1.5
        elif self.maXT[1] == '3': diem_ut = 1
        elif self.maXT[1] == '4': diem_ut = 0
        return diem_ut + self.diem_cm + self.diem_tin*2

    def set_trang_thai(self):
        if self.tong_diem>=18: return "TRUNG TUYEN"
        else: return "LOAI"

    def __repr__(self):
        return self.ma+" "+self.ten+" "+self.chuyen_mon+" "+f"%.1f"%self.tong_diem+" "+self.trang_thai

if __name__ == "__main__":
    n = int(input())
    all_gv = []
    for i in range(n):
        gv = GiaoVien(input(), input(), float(input()), float(input()))
        all_gv.append(gv)
    all_gv.sort(key=lambda x: -x.tong_diem)
    for gv in all_gv:
        print(gv)


