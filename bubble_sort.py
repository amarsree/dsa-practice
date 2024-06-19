# items = [5,3,8,1,6,7,2,-1]

# for j in range(0, len(items)):
#     for i in range(0 , len(items)-1-j):
#         if(items[i]>items[i+1]):
#             items[i], items[i+1] = items[i+1], items[i]

# print(items)

#optimized version 
# added a flat to check if the elements are already sorted or not
items = [1,2,3,-1,2,-3]
flag=False
for j in range(0, len(items)):
    for i in range(0 , len(items)-1-j):
        if(items[i]>items[i+1]):
            items[i], items[i+1] = items[i+1], items[i]
            flag=True
    if(not flag):
        break
    

print(items)

# Time Complexity: O(N2)
# Auxiliary Space: O(1)

# Advantages of Bubble Sort:
# Bubble sort is easy to understand and implement.
# It does not require any additional memory space.
# It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.
# Disadvantages of Bubble Sort:
# Bubble sort has a time complexity of O(N2) which makes it very slow for large data sets.
# Bubble sort is a comparison-based sorting algorithm, which means that it requires a comparison operator to determine the relative order of elements in the input data set. It can limit the efficiency of the algorithm in certain cases.
# Some FAQs related to Bubble Sort:
# What is the Boundary Case for Bubble sort? 
# Bubble sort takes minimum time (Order of n) when elements are already sorted. Hence it is best to check if the array is already sorted or not beforehand, to avoid O(N2) time complexity.
