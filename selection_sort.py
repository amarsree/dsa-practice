#implementing selection sort #1
# def selection_sort(items):
#     for idx,i in enumerate(items):
#         min_idx=idx
#         for jdx,j in enumerate(items[idx+1:]):
#             if(items[jdx+idx+1] < items[min_idx]):
#                 min_idx=jdx+idx+1
#         temp=items[min_idx]
#         items[min_idx] = items[idx]
#         items[idx] = temp
#     print(items)
# selection_sort([5,3,8,6,7,2])

#implementing selection sort #2
# def selection_sort(items):
#     for idx in range(len(items)):
#         min_idx=idx
#         for jdx in range(idx+1,len(items)):
#             if(items[jdx] < items[min_idx]):
#                 min_idx=jdx
#         items[idx],items[min_idx] = items[min_idx],items[idx]
#     print(items)

# selection_sort([5,3,8,1,6,7,2])

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr) ):
            if(arr[j] < arr[min]):
                min = j
        print(arr)
        arr[min], arr[i] = arr[i], arr[min]




selection_sort([5,3,8,1,6,7,2])

# Complexity Analysis of Selection Sort
# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:

# One loop to select an element of Array one by one = O(N)
# Another loop to compare that element with every other Array element = O(N)
# Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)
# Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. The selection sort never makes more than O(N) swaps and can be useful when memory writing is costly. 

# Advantages of Selection Sort Algorithm
# Simple and easy to understand.
# Works well with small datasets.
# Disadvantages of the Selection Sort Algorithm
# Selection sort has a time complexity of O(n^2) in the worst and average case.
# Does not work well on large datasets.
# Does not preserve the relative order of items with equal keys which means it is not stable.
# Frequently Asked Questions on Selection Sort
# Q1. Is Selection Sort Algorithm stable?

# The default implementation of the Selection Sort Algorithm is not stable. However, it can be made stable. Please see the stable Selection Sort for details.

# Q2. Is Selection Sort Algorithm in-place?

# Yes, Selection Sort Algorithm is an in-place algorithm, as it does not require extra space.