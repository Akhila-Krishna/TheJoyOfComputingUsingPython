# Given a number n, you have to write a program that generates a dictionary d which contains (i, i*i), where i is from 1 to n (both included).
# Then you have to just print this dictionary d.

n = int(input())
d = dict()

for i in range(1,n+1):
  d.update({i: i*i})
  
print(d)
