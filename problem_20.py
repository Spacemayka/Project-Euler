# https://projecteuler.net/problem=20

def getFactorial(the_num):
	final_factorial = 1
	for x in range(1, the_num + 1):
		final_factorial *= x
	return final_factorial

def addDigits(factorial):
	string_num = str(factorial)
	digit_sum = 0
	for x in range(0, len(string_num)):
		digit_sum += int(string_num[x])
	return digit_sum

print(addDigits(getFactorial(100)))
