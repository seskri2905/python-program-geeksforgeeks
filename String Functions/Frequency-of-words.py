s = "hello world hello everyone"
res = {}
for word in s.split():
    res[word] = res.get(word,0)+1
print(res)

""" 
Time Complexity:
s.split() => n = length of the string (number of characters). split scans the entire string once => O(N)

for loop => suppose there are k words, the loop runs k times => O(k), but O(k) <= O(N) => O(N)

TC = O(N)

Space Complexity:
List created by split()
Dictionary res 
O(N)

 """