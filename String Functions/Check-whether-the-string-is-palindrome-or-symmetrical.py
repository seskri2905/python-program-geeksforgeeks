str = 'abcabc'
i,j = 0,len(str) - 1
pal = True

while i < j:     # This one time complexity is O(N/2) => O(N). N/2 because the 2 pointer approach stops at middle(i < j fails at middle)
    if str[i] != str[j]:
        pal = False
    i+=1
    j-=1

half = len(str)//2
sym = True
for i in range(half):  # This one time complexity is O(N/2) => O(N). Because half = len(str)//2.
    if len(str) % 2 == 0:
        if str[i] != str[i + half]:
            sym = False
            break
    
    else:
        if str[i] != str[i + half + 1]:
            sym = False
            break

print("Palindrome" if pal else "Not Palindrome")
print("Symmetrical" if sym else "Not Symmetrical")

""" Time Complexity = O(N)
    Space Complexity = O(1)  """