# Using in-built function

""" import math
n = 6
print(math.factorial(n)) """

""" TC = O(N) => n * (n - 1) * (n - 2) .... 1
SC = O(1)  """

# Using for loop

""" n = 6
fact = 1

for i in range(1,n+1):
    fact = fact * i

print(fact) """

""" TC = O(N) => for loop iteration
SC = O(1) """

# Using recursion

n = 6

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(n))

""" TC = O(N) => function call itself
SC = O(N) => Recursion stack  """
