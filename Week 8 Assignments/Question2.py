// Write a Python program to push all zeros to the end of a given list a. The order of the elements should not change.

a = list(input().split())
count = 0

for i in range(len(a)):
    a[i] = int(a[i])
    if(a[i] == 0):
        a.remove(a[i])
        a.append(0)

for i in range(len(a)):
	  print(a[i], end = " ")	
