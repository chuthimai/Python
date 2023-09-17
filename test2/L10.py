print("Ma trận ban đầu")
original_list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(original_list1)
print("Sắp xếp hàng theo thứ tự tăng dần của tổng")
print(sorted(original_list1, key=sum))
print("Ma trận ban đầu")
original_list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print(original_list2)
print("Sắp xếp hàng theo thứ tự tăng dần của tổng")
print(sorted(original_list2, key=sum))