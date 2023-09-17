original_list = [2, 3, 3, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
max = 0
appear = {}
for i in original_list:
    count = original_list.count(i)
    appear[i] = count
    if count > max:
        max = count

for key in appear.keys():
    if appear[key] == max:
        print(key, end=" ")
