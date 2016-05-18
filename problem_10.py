# problem 10: https://projecteuler.net/problem=10

# check if prime
import math
def isPrime(n):
	for x in range(2, int(math.floor(n ** .5 + 1))):
		if n % x == 0:
			return False
	return True

# add all primes under certain number
def addPrimes(n):
	prime_sum = 0
	for x in range (2,n + 1):
		if isPrime(x):
			prime_sum += x
	return prime_sum

print(addPrimes(2000000))