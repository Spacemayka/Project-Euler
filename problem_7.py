def isPrime(n):
	for x in range(2, n/2):
		if n % x == 0:
			return False
	return True

def find_specific_prime(thisPrime):
	prime_counter = 0
	x = 1
	while True:
		x += 1
		if isPrime(x):
			prime_counter += 1
		if prime_counter > thisPrime:
			return x

print(find_specific_prime(10001))



