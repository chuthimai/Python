original_list = [1, 3, 5, 7, 4, 1, 6, 8]
even = None
odd = None
for i in original_list:
    if even!=None and odd!=None:
        break
    elif even==None:
        if i % 2 == 0:
            even = i
    elif odd==None:
        if i % 2 == 1:
            odd = i
print((even, odd))