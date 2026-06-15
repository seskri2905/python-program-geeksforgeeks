a = [1,2,3,1,2,4,5,6,5]
count={}
for n in a:
    count[n] = count.get(n,0) + 1

duplicates = [n for n, c in count.items() if c > 1]
print(duplicates)