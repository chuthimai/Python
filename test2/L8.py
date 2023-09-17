def select_column(arr: list, n: int):
    res = []
    for i in arr:
        res.append(i[n-1])
    return res

print("Danh sách ban đầu")
original_list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(original_list1)
print("1st column:")
print(select_column(original_list1, 1))
print("Danh sách ban đầu")
original_list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print(original_list2)
print("3rd column:")
print(select_column(original_list2, 3))
