def count(num):
    occured_ele = {}  # Initialize dictionary
    for i in num:
        if i in occured_ele:
            occured_ele[i] += 1  # Increment count if element exists
        else:
            occured_ele[i] = 1  # Initialize count for new element
    return occured_ele

data = [10, 20, 3, 1, 0, 20, 40, 30, 4, 50]
occ = count(data)
print(occ)




    
