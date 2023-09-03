# PY01016 GIẢI MÃ

times = int(input().split()[0])

for i in range(times):
    string = input()
    char_before = string[0]
    for i_th in range(1, len(string)):
        if string[i_th].isdigit():
            for j in range(0, int(string[i_th])):
                print(char_before, end='')
        else:
            char_before = string[i_th]
    print()

