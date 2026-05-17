""" Input: arr = [12, 10, 5, 6, 52, 36], k = 2  
Output: [5, 6, 52, 36, 12, 10]
Explanation: Split the array at index k and move the first part [12, 10] (for k = 2) to the end. """

arr = [12, 10, 5, 6, 52, 36]

k = 2

arr = arr[k:] + arr[:k]

print(arr)


""" 
TC = O(n-k) + O(k) + O(n) => O(N)  O(n-k) is from arr[k:] and O(k) is from the arr[:k] and O(N) is from the concatenation  
SC = O(N) => O(N) is from the Concatenation """