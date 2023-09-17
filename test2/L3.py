original_list = ['Red', 'Green', 'Blue', 'White', 'Black']
for i in range(len(original_list)):
    original_list[i] = original_list[i][::-1]
print(original_list)