
class Student:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diemCC = None
        self.ghi_chu = None

    def tinh_diemCC(self, diem_danh: str):
        diem_danh = diem_danh.lower()
        vang = diem_danh.count("v")
        muon = diem_danh.count("m")
        self.diemCC = 10 - vang*2 - muon
        if self.diemCC <= 0:
            self.diemCC = 0
            self.ghi_chu = "KDDK"

    def __repr__(self):
        try:
            return self.ma + " " + self.ten + " " + self.lop + " " + str(self.diemCC) + " " + self.ghi_chu
        except TypeError:
            return self.ma + " " + self.ten + " " + self.lop + " " + str(self.diemCC)

class QuanLyHS:
    def __init__(self):
        self.ds_hs = []

    def tinhCC(self, mhs: str, diem_danh: str):
        for i in range(len(self.ds_hs)):
            if self.ds_hs[i].ma == mhs:
                self.ds_hs[i].tinh_diemCC(diem_danh)

    def print_all_list(self):
        for hs in self.ds_hs:
            print(hs)


if __name__ == "__main__":
    n = int(input())
    all_students = []
    for i in range(n):
        student = Student(input(), input(), input())
        all_students.append(student)
    quan_ly = QuanLyHS()
    quan_ly.ds_hs = all_students
    for i in range(n):
        msv, diem_danh = input().split()
        quan_ly.tinhCC(msv, diem_danh)
    quan_ly.print_all_list()