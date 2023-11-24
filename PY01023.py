# PY01023 - PHÂN TÍCH THỪA SỐ NGUYÊN TỐ

def phan_tich():
    n = int(input())
    print("1", end=" ")
    i = 2
    dem = 0
    write = True
    if n != 1:
        while n != 1:
            if n%i == 0:
                dem += 1
                n = n/i
                write = False
            else:
                if not write:
                    print(f"* {i}^{dem}", end=" ")
                    write = True
                    dem = 0
                i += 1

        print(f"* {i}^{dem}", end=" ")

if __name__ == '__main__':
    n = int(input())
    for i in range(n): phan_tich(); print();




