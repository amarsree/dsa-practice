items =  [5,3,8,1,6,7,2]


def mergeSort(items):
    if len(items) > 1:
        left_array = items[:len(items)//2]
        right_array = items[len(items)//2:]

        mergeSort(left_array)
        mergeSort(right_array)

        i=0
        j=0
        k=0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                items[k] = left_array[i]
                i += 1
            else:
                items[k] = right_array[j]
                j += 1
            k += 1
        
        while i < len(left_array):
            items[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            items[k] = right_array[j]
            j += 1
            k += 1



mergeSort(items)
print(items)







