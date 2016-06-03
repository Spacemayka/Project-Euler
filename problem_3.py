
# create loop of numbers increasing
# divide THENUMBER by each of those numbers  
# check if the mod is equal to zero
# output number that is the quotient of that number
# check if number is prime
# print

import math

def isPrime(n):
	for x in range(2, int(math.ceil(n/2))):
		if n % x == 0:
			return False
	return True

def FindLargestPrimeFactor(the_num):	
	for counter in range(1, the_num):
		if the_num % counter == 0:
			quotient = the_num / counter
			if isPrime(quotient):
				return quotient

print(FindLargestPrimeFactor(600851475143))
