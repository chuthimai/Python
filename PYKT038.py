# PYKT038 - HỆ CƠ SỐ 8

num2 = input()
num2 = "0"* ((3 - len(num2)%3)%3)+ num2

l = {
    "000": "0", "001": "1", "010": "2", "011": "3",
    "100": "4", "101": "5", "110": "6", "111": "7"
}

num8 = ""
for i in range(0, len(num2), 3):
    num8 += l[num2[i:i+3]]

print(num8)