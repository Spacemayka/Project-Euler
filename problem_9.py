# make a loop to check all the possible numbers for 3 integers
def cycle_triplets():
	for x in range(1,1000):
		for y in range(1,1000):
			for z in range(1,1000):
				if is_pythagorean_triplet(x, y, z) and is_sum_1000(x, y, z):
					return x * y * z

# check if they are a pythagorean triple
def is_pythagorean_triplet(x, y, z):
	if x ** 2 + y ** 2 == z ** 2:
		return True
	else:
		return False

# check if they add up to 1000
def is_sum_1000(a,b,c):
	if a + b + c == 1000:
		return True
	else:
		return False


print(cycle_triplets())

