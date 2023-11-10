# PY02020 TÍNH ĐIỂM TRUNG BÌNH

n = int(input().split()[0])
diem = list(map(float, input().split()[:n]))
diem = sorted(diem)
nho_nhat = diem[0]
lon_nhat = diem[-1]

while nho_nhat in diem:
    diem.remove(nho_nhat)
while lon_nhat in diem:
    diem.remove(lon_nhat)
diemTB = sum(diem)/len(diem)
print(f"%.2f" % diemTB)


