# In this assignment, you will be provided with the number of rows i.e. r and columns i.e. c as the input and your job is to create a matrix of size rxc.
# Also, the matrix should have elements starting from 1 to rxc with an increment of one in row manner.

r,c = input().split()
r = int(r)
c = int(c)

R=[]
u=1
for i in range(r):
    C=[]
    for j in range(c):
        C.append(u)
        u=u+1
    R.append(C)
for k in range(r):
    for l in range(c):
        if l!=c-1:
            print(R[k][l],end=" ")
        else:
            print(R[k][l],end="")
    if k!=r-1:
    	print()
