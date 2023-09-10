# PY01018 - MÃ HÓA 2

P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def encode(string: str, k: int) -> str:
    global P
    encode_str = ""
    for char in string:
        encode_str += P[(P.find(char)+k) % 28]
    return encode_str[::-1]

if __name__ == "__main__":
    isTrue = True
    while isTrue:
        data = input().split()
        k = int(data[0])
        if k == 0:
            isTrue = False
            continue
        string = data[1]
        print(encode(string, k))
