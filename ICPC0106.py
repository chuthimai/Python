def base2(bin_num):
    return bin_num


def base4(bin_num):
    while len(bin_num) % 2:
        bin_num = '0' + bin_num
    num = {'00': '0', '01': '1', '10': '2', '11': '3'}
    num_base4 = ''
    for i in range(0, len(bin_num), 2):
        num_base4 = num_base4 + num[bin_num[i:i+2]]
    return num_base4


def base8(bin_num):
    while len(bin_num) % 3:
        bin_num = '0' + bin_num
    num = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
    num_base8 = ''
    for i in range(0, len(bin_num), 3):
        num_base8 = num_base8 + num[bin_num[i:i+3]]
    return num_base8


def base16(bin_num):
    while len(bin_num) % 4:
        bin_num = '0' + bin_num
    num = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
           '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    num_base16 = ''
    for i in range(0, len(bin_num), 4):
        num_base16 = num_base16 + num[bin_num[i:i+4]]
    return num_base16


times = int(input())
for i in range(times):
    base = input()
    bin_num = input()
    if base == '2':
        print(base2(bin_num))
    elif base == '4':
        print(base4(bin_num))
    elif base == '8':
        print(base8(bin_num))
    elif base == '16':
        print(base16(bin_num))


