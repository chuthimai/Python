# PY04015 - LẬP HÓA ĐƠN - 1

sMa = 1
class Customer:
    def __init__(self, ten, so_dau, so_cuoi):
        global sMa
        self.ma = f"KH%02d" % sMa
        sMa += 1
        self.ten = ten
        self.so_nuoc = so_cuoi - so_dau
        self.tien = self.tinh_tien()

    def tinh_tien(self) -> float:
        res = 0
        if self.so_nuoc <= 50:
            res = 100*self.so_nuoc*1.02
        elif self.so_nuoc <= 100:
            res = (100*50 + 150*(self.so_nuoc-50))*1.03
        else:
            res = (100*50 + 150*50 + 200*(self.so_nuoc-100))*1.05
        return res

    def __repr__(self):
        return self.ma+" "+self.ten+" "+str(round(self.tien))

if __name__ == "__main__":
    n = int(input())
    all_cus = []
    for i in range(n):
        all_cus.append(Customer(input(), int(input()), int(input())))

    all_cus.sort(key=lambda x: -x.tien)
    for cus in all_cus: print(cus)


