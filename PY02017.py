# PY02017 - TÂN SUẤT LẺ

def one_time():
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    set = {i for i in arr}
    for i in set:
        if arr.count(i) % 2 == 1:
            print(i)
            break

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        one_time()



