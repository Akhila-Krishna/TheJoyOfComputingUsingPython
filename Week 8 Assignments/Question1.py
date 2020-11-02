// Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.

def addup(n):
    sumdig = 0
    for digit in str(n):
        sumdig += int(digit)
    return sumdig
    
n = int(input())

while(len(str(n)) != 1):
    n = addup(n)

print(n)
