# Iterative Binary Search

""" def binarySearch(arr,x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binarySearch(arr,x)

    if result != -1:
        print("Element found. The index is:", result)
    else:
        print("Element not found") """

""" Time Complexity:
Binary search is the divide and conquer approach

Best case will be 0(1), if the target element = middle element
Average case will be O(Log N), if the size of the array is cut in half or divided, then it is O(Log N)

Space Complexity:
Creating variables will take O(1). So, the space complexity is O(1) """