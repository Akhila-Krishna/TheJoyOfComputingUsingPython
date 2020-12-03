# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence

import math

C = 50
H = 30
Q = []
D = list(input().split(","))
for i in range(len(D)):
	D[i] = int(D[i])
	a = math.sqrt((2*C*D[i])/H)
	b = math.modf(a)
	#print(b[0])
	if(b[0] >= 0.5):
		Q.append(math.ceil(a))
	else:
		Q.append(math.floor(a))
	if(i != len(D)-1):
		print(Q[i], end=",")
	else:
		print(Q[i])
