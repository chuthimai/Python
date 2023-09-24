# PY02031 - KIỂM TRA NGUYÊN TỐ

def is_prime(n: int) -> bool:
    if n < 2: return False
    elif n == 2: return True
    elif pow(2, n-1, n) == 1: return True
    else: return False

n, m = [int(i) for i in input().split()]
matrix = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
for row in range(n):
    for column in range(m):
        if is_prime(matrix[row][column]): print("1 ", end="")
        else: print("0 ", end="")
    print()



