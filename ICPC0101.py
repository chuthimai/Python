element = int(input())
array = input()
array = array.split(' ')
array = [int(i) for i in array]


def del_pair():
    global array
    i = 0
    while i+1 < len(array):
        if (array[i] + array[i+1]) % 2 == 0:
            array.pop(i+1)
            array.pop(i)
        else:
            i += 1
    return len(array)


l = len(array)
l_after = del_pair()
while l != l_after:
    l = l_after
    l_after = del_pair()
print(l)