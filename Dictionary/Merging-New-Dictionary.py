d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

merge_values = d1 | d2

print(merge_values)

""" 
TC:
Python creates a new dictionary called as merge_values

copy all the elements of d1, insert/update all elements in d2

m = len(d1)
n = len(d2)

O(m) + O(n) => O(m + n)

SC:
Python creates a new dict

O(m) + O(n) => O(m + n)


 """