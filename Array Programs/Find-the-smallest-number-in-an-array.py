arr = [5,4,1,2,3]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i
    
print(f"the smallest no. is {smallest} and found in position {arr[i]}")