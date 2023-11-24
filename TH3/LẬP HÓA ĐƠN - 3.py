
class Item:
    def __init__(self, ma, ten, so_luong, don_gia, chiet_khau):
        self.ma = ma
        self.ten = ten
        self.so_luong = so_luong
        self.don_gia = don_gia
        self.chiet_khau = chiet_khau
        self.tong_tien = self.don_gia*self.so_luong - self.chiet_khau

    def __repr__(self):
        return self.ma+" "+self.ten+" "+str(self.so_luong)+" "+str(self.don_gia)+" "+str(self.chiet_khau)+" "+str(self.tong_tien)

if __name__ == '__main__':
    n = int(input())
    list_i = []
    for i in range(n):
        item = Item(input(), input(), int(input()), int(input()), int(input()))
        list_i.append(item)
    list_i.sort(key=lambda x: (-x.tong_tien))
    for item in list_i:
        print(item)