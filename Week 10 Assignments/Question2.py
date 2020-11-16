# Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates. 

a = list(input().split())
n = len(a)

i, total = 0, 1

for i in range(2, n + 2): 
	total += i 
	total -= int(a[i - 2])

print(total)
