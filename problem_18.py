# https://projecteuler.net/problem=18
import itertools
import math
import numpy as np

def getBinaryList(pyramid_size):
	my_list = ["".join(seq) for seq in itertools.product("01", repeat = pyramid_size)]
	return my_list

# print(getBinaryList(15))

# create grid with pyramid
# make loop that reads off binary numbers and moves down the pyramid accordingly
# add up the values in the given route
# if statement testing if the sum is bigger than "biggestSum"

my_list = '75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

def createGrid(grid_size):
	my_grid = np.zeros((grid_size + 1, grid_size + 1)) # returns an array with those demensions filled with zeros
	return my_grid

# print(createGrid(4)) 

def pyramidToList(pyramid):
	pyramid = list(map(int, pyramid.split()))
	return pyramid

# print (pyramidToList(my_list))

def populateGrid(pyramid_list, my_grid, length):
	true_index = 0
	for index, num in enumerate(pyramid_list):
		if index == length + 1:
			break
		for small_index, start_num in enumerate(range(true_index, true_index + index)):
			my_grid[index, small_index] = pyramid_list[true_index + small_index] 
			# print (my_grid[small_index, index])
			# print(my_grid)
		true_index += index
	# print(true_index)
	return my_grid

# populateGrid(pyramidToList(my_list), createGrid(5), 5)

def findGreatestSum(final_grid, binary_list, pyramid_height, first_number):
	largest_sum = 0
	for paths in binary_list:
		temp_sum = first_number
		x = 1
		y = 0
		for index, rows in enumerate(range(0, pyramid_height - 1)):
			if int(paths[index]) == 1:
				y += 1
			x += 1
			temp_sum += final_grid[x, y]
		if temp_sum > largest_sum:
			largest_sum = temp_sum
	return largest_sum

print(findGreatestSum(populateGrid(pyramidToList(my_list), createGrid(15), 15), getBinaryList(15), 15, 75))








# def iterList(list_of_binaries):
