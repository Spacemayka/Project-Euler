# https://projecteuler.net/problem=15

# create a grid
# make move right and move down that outputs the new location
# recusively call the move right and move down with an if statement about being in the bottom right then the counter gets a + 1
# make if statements about being on the side of the grid so you could definitely know when you have to go right or down

# def createBetterGrid(grid_size):
# 	new_grid = []
# 	big_counter = 0
# 	counter = 0
# 	point = 0
# 	while True:
# 		new_grid.append((point, counter))
# 		point += 1
# 		big_counter += 1
# 		if point >= grid_size + 1:
# 			counter += 1
# 			point = 0
# 		if point == grid_size and counter == grid_size:
# 			new_grid.append((grid_size, grid_size))
# 			return new_grid

# def start_location(new_grid):
# 	start = (0, 0)
# 	return start

# def make_move(current_location, move):


# print(createBetterGrid(2))



# make a nested loop that starts iterating at (x, y) x = 0, for y upto len(grid) then do that for all x up to len(grid), and count each iteration

# def get_paths(grid_length):
# 	x = 0
# 	y = 0
# 	z = 0
# 	counter = 0
# 	for x in range(0, 2):
# 		for y in range(0, 2):
# 			counter += 1
# 			for z in range(0, 2):
# 				counter += 1
# 				print (x, y, z)
# 		counter += 1
# 	return counter

# print (get_paths(3))



# def populate_moves(grid_size):
# 	move_list = []
# 	for x in range(0, grid_size):
# 		move_list.append(0)
# 		move_list.append(1)
# 	return move_list

# def get_permutations(my_list):
	#return len(list(set(list(itertools.permutations(my_list, len(my_list))))))

# def count_paths(a_list):
# 	count = 0
# 	for items in a_list:
# 		if a_list.count(0) == a_list.count(1):
# 			count += 1
# 	return count

# print(get_permutations(populate_moves(6)))

# def get_count(grid_size):
# 	count = 0
# 	my_list = ["".join(seq) for seq in itertools.product("01", repeat = grid_size * 2)]
# 	for items in my_list:
# 		if items.count('0') == items.count('1'):
# 			count += 1
# 	return count

# print(get_count(11))

# def kbits(n, k):
#     result = []
#     for bits in itertools.combinations(range(n), k):
#         s = ['0'] * n
#         for bit in bits:
#             s[bit] = '1'
#         result.append(''.join(s))
#     return len(result)

# print (kbits(26, 13))

import time
import itertools
import numpy as np

def createGrid(grid_size):
	my_grid = np.zeros((grid_size + 1, grid_size + 1)) # returns an array with those demensions filled with zeros
	return my_grid

# new_grid = createGrid(20)
# current_location = new_grid[0,0]

def iterGrid(my_grid):
	for x in range(0, 21):
		my_grid[x, 0] = 1
	for y in range(0, 21):
		my_grid[0, y] = 1
	for x in range(1,21):
		for y in range(1,21):
			my_grid[x, y] = my_grid[x-1, y] + my_grid[x, y-1]
	return my_grid

print(iterGrid(createGrid(20)))
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))



