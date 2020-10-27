# In this assignment, you have to write a program to print a pattern of numbers.
# The input should be the number of rows.
# Your program should print this pattern where the first row contains only one element i.e 1.
# The second row should contain two elements i.e. 1 and 2 separated by a space.
# The third row should contain three elements i.e. 1, 2 and 3 separated by a space.

n = int(input())
for row in range(1, n+1):
	for column in range(1, row+1):
		if(column != row):
			print(column, end = ' ')
		else:
			print(column)
