def getExponent(my_num, exponent):
	return (my_num**exponent)

# print(getExponent(2,1000))

def add_digits(my_num, exponent):
	num = getExponent(my_num, exponent)
	lst = [int(i) for i in str(num)]
	sum = 0
	for number in lst:
		sum += number
	return sum


print(add_digits(2, 1000))
