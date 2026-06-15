str = "apple"
i,j = 0,len(str)-1
is_palindrome = True

while i < j:
    if str[i] != str[j]:
        is_palindrome = False
        break
    i+=1
    j-=1

if is_palindrome:
    print('yes')
else:
    print('no')


""" 
TC = O(N/2) => O(N) 
SC = O(N)
"""