# Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

import math

Q = list(input().split(","))
Q.sort()
for i in range(len(Q)):
  if(i != len(Q)-1):
      print(Q[i], end=",")
  else:
      print(Q[i])
