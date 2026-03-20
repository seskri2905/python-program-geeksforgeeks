import math

n = int(input('Enter the number:'))

def isFibonacci(n):
    return isPerfectSquare(5 * n ** 2 + 4) or isPerfectSquare(5 * n ** 2 - 4)   # Arithmetic Operation O(1)

def isPerfectSquare(value):
    s =  int(math.sqrt(value))    # O(1)
    return s * s == value

result = isFibonacci(n)

if result:
    print(f'{n} is a fibonacci number')
else:
    print('No')

""" TC = O(1)
SC = O(1) """