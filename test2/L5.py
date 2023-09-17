
def isOnly(arr: list)->bool:
    isTrue = True
    for i in arr:
        count = arr.count(i)
        if count!=1:
            isTrue = False
            break
    return isTrue

original_list1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
original_list2 = [2, 4, 6, 8, 10, 12, 14]
print(isOnly(original_list1))
print(isOnly(original_list2))

