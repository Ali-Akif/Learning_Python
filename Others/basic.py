array_1 = [1,4,6,8,9,10]
array_2 = [2,3,5,7,8,11,12]
sorted_array = []
index1= index2 = 0

while index1 < len(array_1) and index2 < len(array_2):
    
    if array_1[index1] < array_2[index2]:
        sorted_array.append(array_1[index1])
        index1 += 1
    else:
        sorted_array.append(array_2[index2])
        index2 += 1
    
sorted_array.extend(array_1[index1:])
sorted_array.extend(array_2[index2:])

print(sorted_array)