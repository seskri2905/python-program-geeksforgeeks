""" arr = [1,2,3,4,5,6,7,8]
d = 2
n = len(arr)
arr.reverse()      # Reversing an array O(N)

arr[:n-d] = arr[:n-d][::-1]    # Creating a slice,reversing a slice and Assigning back 
arr[n-d:] = arr[n-d:][::-1]    # Creating a slice,reversing a slice and Assigning back

print(arr) """

""" TC = O(N)
SC = O(N)  # Because storing array values """

arr = [1,2,3,4,5,6,7,8]
d = 2
n = len(arr)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Step 1: Reverse whole array
reverse(arr, 0, n-1)

# Step 2: Reverse first d elements
reverse(arr, 0, d-1)

# Step 3: Reverse remaining elements
reverse(arr, d, n-1)

print(arr)

""" TC = O(N)
SC = O(1) """