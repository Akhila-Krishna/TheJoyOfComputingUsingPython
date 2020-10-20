# Write a program to find whether a given number is a power of 2 or not.

n = int(input())
while(1):
	n = n/2
	if(n == 1):
		print("YES")
		break
	elif(n == 0):
		print("NO")
		break
	else:
		continue
