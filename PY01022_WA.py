# PY01022 - TỔNG CHỮ SỐ

def sum_digit(num: str):
    total = 0
    for digit in num:
        total += int(digit)
    return total

n = abs(int(input()))
step = 0
if n <= 9: step = 1
while n >= 10:
    step += 1
    n = sum_digit(str(n))

print(step)



