items = [5,3,8,1,6,7,2,-1]

for j in range(0, len(items)):
    for i in range(0 , len(items)-1-j):
        if(items[i]>items[i+1]):
            items[i], items[i+1] = items[i+1], items[i]

print(items)
