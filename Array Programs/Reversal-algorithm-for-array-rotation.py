arr = [1,2,3,4,5,6,7]
d = 2
n = len(arr)

def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1

# Handle cases where d > n
d = d % n

# Step 1: Reverse first d elements
reverse(arr,0,d-1)   # [2,1,3,4,5,6,7]

# Step 2: Reverse remaining elements
reverse(arr,d,n-1) # [2,1,7,6,5,4,3]

# Step 3: Reverse entire array
reverse(arr,0,n-1) # [3,4,5,6,7,1,2]    

print(arr)

""" TC = O(d + n-d + n) => O(2n) => O(N)
    SC = O(1) """