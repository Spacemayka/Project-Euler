# https://projecteuler.net/problem=12

import math

# input number, output number of divisors
def countFactors(the_num):	
	counter = 0
	for index in range(1, int(math.sqrt(the_num)) + 1):
		if the_num % index == 0:
			counter += 1
	return counter + 1





# test
print(countFactors(4))

