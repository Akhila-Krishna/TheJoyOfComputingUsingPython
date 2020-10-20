# A lower triangular matrix is a square matrix (where the number of rows and columns are equal)  where all the elements above the diagonal are zero.

# For example, the following is a lower triangular matrix with the number of rows and columns equal to 3.
#     1 0 0
#     4 5 0
#     7 8 9

# Write a program to convert a square matrix into a lower triangular matrix.

n = int(input())
x = []
m = []
for i in range(n):
	x = list(input().split())
	for j in range(i+1,n):
		x[j] = 0
	m.append(x)
for i in range(n):
	for j in range(n):
		print(m[i][j], end="")
		if(j != (n-1)):
			print(end=" ")
	if(i != (n-1)):
		print(end="\n")
