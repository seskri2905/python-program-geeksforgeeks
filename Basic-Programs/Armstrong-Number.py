import math
num = int(input('Enter a Number'))
n = num
power = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total = total + math.pow(digit,power)
    n = n // 10

print(total)
if num == total:
    print('Armstrong')
else:
    print('Not a Armstrong')

""" TC = O(log base 10 N) => while condn. is dependent on the n = n // 10
SC = O """