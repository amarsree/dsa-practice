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
def selection_sort(items):
    for idx in range(len(items)):
        min_idx=idx
        for jdx in range(idx+1,len(items)):
            if(items[jdx] < items[min_idx]):
                min_idx=jdx
        items[idx],items[min_idx] = items[min_idx],items[idx]
    print(items)

selection_sort([5,3,8,1,6,7,2])
