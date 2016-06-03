# https://projecteuler.net/problem=12

import math

# input number, output number of divisors
def countFactors(the_num):	
	counter = 0
	for index in range(1, int(math.floor(math.sqrt(the_num))) + 1):
		if the_num % index == 0:
			counter += 1
	if index ** 2 == the_num:
		return counter * 2 - 1	
	return counter * 2 

# function that gets a certain triangle number 
# def getTriangle(tri_num):

def getTriangle(my_num):
	my_divisor = 0
	temp_count = 0
	while True:
		temp_count += 1
		my_divisor += temp_count
		if countFactors(my_divisor) >= my_num:
			return(my_divisor)

print(getTriangle(500))





# start at the square of the number given, and check every number after ifTriangle and for divisors > 500 and 




# test
# print(countFactors(30))

