s = "This is a Python Program"

words = s.split()

even_words = [w for w in words if len(w) % 2 == 0]

res = ' '.join(even_words)

print(res)

""" 
TC = O(N)
SC = O(N)
 """