# PY01073 HOÁN VỊ KÝ TỰ

def generate_permutations(S):
    if len(S) == 1:
        return [S]

    permutations = []
    for i in range(len(S)):
        first_char = S[i]
        rest_chars = S[:i] + S[i+1:]
        rest_permutations = generate_permutations(rest_chars)
        for perm in rest_permutations:
            permutations.append(first_char + perm)

    return permutations

S = input()
permutations = generate_permutations(S)

for perm in permutations:
    print(perm)
