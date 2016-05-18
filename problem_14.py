# https://projecteuler.net/problem=14

def collatzSolver(my_num):
	original_num = my_num
	count = 0
	while True:
		if my_num == 1:
			count += 1
			return (count, original_num)
		elif my_num % 2 == 0:
			my_num /= 2
			count += 1
		elif my_num % 2 == 1:
			my_num = my_num * 3 + 1
			count += 1


#print(collatzSolver(13))

def findLongestCollatz(my_range):
	longest_collatz = 0
	current_name = 0
	for index in range(1, my_range + 1):
		current_collatz = collatzSolver(index)[0]
		current_name = collatzSolver(index)[1]
		if current_collatz > longest_collatz:
			longest_collatz = current_collatz
			longest_name = current_name
	return (longest_name, longest_collatz)



print(findLongestCollatz(1000000))