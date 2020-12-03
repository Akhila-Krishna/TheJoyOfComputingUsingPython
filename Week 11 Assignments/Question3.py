# Write a program, which will find all such numbers between m and n (both included) such that each digit of the number is an even number.

m, n = input().split(",")
m = int(m)
n = int(n)
A = []
i = m
flag = 0
while(i>=m and i<=n):
	num = str(i)
	for digits in num:
		digits = int(digits)
		if(digits%2 != 0):
			flag = 1
			break
		else:
			continue
	if(flag == 0):
		A.append(i)
	i += 1
	flag = 0

for k in range(len(A)):
	if(k != len(A)-1):
		print(A[k], end=",")
	else:
		print(A[k])
