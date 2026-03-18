""" lower_limit = int(input('Enter Lower Limit:'))
upper_limit = int(input('Enter Upper Limit'))

prime_number = []

for num in range(lower_limit,upper_limit+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            prime_number.append(num)

print(prime_number) """

""" TC = O(N^2), Because The outer loop runs N times and the inner loop runs up to N times
SC = O(N) due to storing prime numbers in a list """

x, y = 2, 16
primes = [True] * (y + 1)

primes[0],primes[1] = False,False

for i in range(2,int(y ** 0.5)+1):
    if primes[i]:
        for j in range(i * i,y + 1,i):
            primes[j] = False

res = [i for i in range(x,y+1) if primes[i]]
print(res if res else 'No')

