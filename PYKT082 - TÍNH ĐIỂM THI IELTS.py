def convert(correct_answer):
    if correct_answer >= 39: return 9.0
    elif correct_answer >= 37: return 8.5
    elif correct_answer >= 35: return 8.0
    elif correct_answer >= 33: return 7.5
    elif correct_answer >= 30: return 7.0
    elif correct_answer >= 27: return 6.5
    elif correct_answer >= 23: return 6.0
    elif correct_answer >= 20: return 5.5
    elif correct_answer >= 16: return 5.0
    elif correct_answer >= 13: return 4.5
    elif correct_answer >= 10: return 4.0
    elif correct_answer >= 7: return 3.5
    elif correct_answer >= 5: return 3.0
    elif correct_answer >= 3: return 2.5

def round_num(num):
    num = num*100
    if num%100<25:
        num = num//100 * 100
    elif num%100<75:
        num = num//100 * 100 + 50
    elif num%100<100:
        num = num//100 * 100 + 100
    return round(num/100, 1)

def one_time():
    r, l, s, w = map(float, input().split())
    r = convert(r)
    l = convert(l)
    diemTB = (r + l + s + w)/4
    diemTB = round_num(diemTB)
    print(diemTB)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        one_time()






