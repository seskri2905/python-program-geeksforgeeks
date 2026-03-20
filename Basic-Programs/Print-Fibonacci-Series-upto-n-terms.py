n = int(input('Enter a number:'))

a = 0
b = 1
print(a, b, end=' ')

count = 1
next = b

while count < n - 1:
    print(next,end=' ')
    a,b = b,next
    next = a + b
    count += 1

""" TC = O(N)
SC = O(1) """   