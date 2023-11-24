# PY01046 - THÁP HÀ NỘI

def di_chuyen(so_coc, goc, dich, cot_phu):
     if so_coc == 1:
         print(f"{goc} -> {dich}")
         return

     di_chuyen(so_coc-1, goc, cot_phu, dich)
     print(f"{goc} -> {dich}")
     di_chuyen(so_coc-1, cot_phu, dich, goc)

if __name__ == '__main__':
    n = int(input())
    di_chuyen(n, "A", "C", "B")






