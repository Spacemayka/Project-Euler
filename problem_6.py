# find the sum of the squares

def findSumOfSquares(n):
	mysum = 0
	for x in range(1, n + 1):
		mysum += x ** 2
	print(mysum)
	return mysum

def findSquareOfSums(n):
	mysquare = 0
	for x in range(1, n + 1):
		mysquare += x
	mysquare = mysquare ** 2
	print(mysquare)
	return mysquare

def findDifference(n, m):
	return abs(n - m)

print(findDifference(findSumOfSquares(100), findSquareOfSums(100)))




# find the square of the sums
# fint the difference between the two
