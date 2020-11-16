# Given a list A of elements of length N, ranging from 1 to N. All elements may not be present in the array. 
# If the element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present display -1 at that place.

a = list(input().split())
n = len(a)
b = [-1]*n

for i in range(n):
    if(str(i) in a):
        b[i] = i
    print(b[i], end = " ")
