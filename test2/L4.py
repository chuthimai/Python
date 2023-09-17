def intersection(arr1: list, arr2: list)->list:
    res = []
    for i in arr1:
        if i in arr2:
            res.append(i)
    return res

original_list = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
res = original_list[0]
for arr in original_list:
    res = intersection(res, arr)
print(res)