# PY01017 - MÃ HÓA 1

def encode(string: str) -> str:
    encode_str = ""
    string += "/"
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            encode_str += str(count) + string[i-1]
            count = 1
    return encode_str

if __name__ == "__main__":
    times = int(input().split()[0])
    for i in range(times):
        string = input()
        print(encode(string))


