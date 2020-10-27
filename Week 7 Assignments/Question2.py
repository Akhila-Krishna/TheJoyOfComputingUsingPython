# Given a square matrix with n rows and n columns, you have to write a program to rotate this matrix such that each element is shifted by one place 
# in a clockwise manner.

n = int(input())
m = []
a = []
for i in range(n):
    a = list(input().split())
	  m.append(a)
    
top = 0
bottom = n-1
left = 0
right = n-1

while left < right and top < bottom: 
    prev = int(m[top+1][left])
    for i in range(left, right+1):
        curr = int(m[top][i])
        m[top][i] = prev
        prev = curr
    top += 1

    for i in range(top, bottom+1): 
        curr = int(m[i][right]) 
        m[i][right] = prev 
        prev = curr 
    right -= 1

    for i in range(right, left-1, -1): 
        curr = int(m[bottom][i]) 
        m[bottom][i] = prev 
        prev = curr 
    bottom -= 1

    for i in range(bottom, top-1, -1): 
        curr = int(m[i][left]) 
        m[i][left] = prev 
        prev = curr 
    left += 1

for i in range(n):
    for j in range(n):
        print(m[i][j], end="")
        if(j != (n-1)):
            print(end=" ")
    if(i != (n-1)):
        print(end="\n")
