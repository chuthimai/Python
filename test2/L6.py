def is_sort(arr: list)->bool:
    isTrue = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            isTrue = False
            break
    return isTrue

original_list1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
original_list2 = [1, 2, 4, 6, 8, 10, 12, 14, 18, 17]

print(is_sort(original_list1))
print(is_sort(original_list2))