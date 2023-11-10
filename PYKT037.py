# PYKT037 - ĐỔI CƠ SỐ

so_du = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ,'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        res = []
        N, b = map(int, input().split())
        while N != 0:
            res.append(so_du[N % b])
            N = N // b

        for j in res[::-1]:
            print(j, end="")
        print()



