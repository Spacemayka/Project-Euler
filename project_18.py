# https://projecteuler.net/problem=18

def get_count(pyramid_size):
	count = 0
	my_list = ["".join(seq) for seq in itertools.product("01", repeat = pyramid_size)]
	return my_list

print(get_count(3))