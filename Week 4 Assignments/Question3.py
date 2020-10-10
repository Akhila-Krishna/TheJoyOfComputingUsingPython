# In this assignment, you will sort a list let's say list_1 of numbers in increasing order using the random library.

# Following are the steps to sort the numbers using the random library.
# Step 1: Import the randint definition of the random library of python. Check this page if you want some help.
# Step 2: Take the elements of the list_1 as input.
# Step 3: randomly choose two indexes i and j within the range of the size of list_1.
# Step 4: Swap the elements present at the indexes i and j. After doing this, check whether the list_1 is sorted or not.
# Step 5: Repeat step 3 and 4 until the array is not sorted.

from random import randint
n =int(input())
l =[]
for i in range(n):
    ip=int(input())
    l.append(ip)
S=True
u=sorted(l)
while(S):
    j=randint(0,n-1)
    i=randint(0,n-1)
    ab=l[j]
    l[j]=l[i]
    l[i]=ab
    if l==u:
      S=True
    else:
      S=False
      
    if(S):
        break
    else:
        S=True
for b in range(n):
    if(b==n-1):
        print(l[b],end="")
    else:
        print(l[b],end=" ")
