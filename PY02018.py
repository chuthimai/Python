# PY02018 - SỐ NHỎ NHẤT CÒN THIẾU

if __name__ == '__main__':
    n = int(input())
    arr = list({int(i) for i in input().split()[:n]})
    is_found = False
    if arr[0] > 1:
        print(1)
        is_found = True
    else:
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != 1:
                print(arr[i-1]+1)
                is_found = True
                break
    if not is_found:
        print(arr[n-1]+1)





