# PY01072 BÀI TOÁN TỔ HỢP

from itertools import combinations

def generate_combinations(arr, k):
    unique_elements = list(set(arr))
    unique_elements.sort()
    result = list(combinations(unique_elements, k))
    return result

N, K = map(int, input().split())
A = list(map(int, input().split()))

combinations_list = generate_combinations(A, K)

for comb in combinations_list:
    print(*comb)
