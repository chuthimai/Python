def oneTime():
    elements = int(input())
    array = input().split()
    array = sorted([int(i) for i in array])
    res = 0

    for i in range(0, elements-2):
        # initialize left and right
        l = i + 1
        r = elements - 1
        x = array[i]
        while l < r:
            if x + array[l] + array[r] == 0:
                res += 1
                l += 1

            # If sum of three elements is less
            # than zero then increment in left
            elif x + array[l] + array[r] < 0:
                l += 1

            # if sum is greater than zero then
            # decrement in right side
            else:
                r -= 1

    print(res)


if __name__ == '__main__':
    times = int(input())
    for i in range(times):
        oneTime()