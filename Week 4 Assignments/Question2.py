# In this program, you have to calculate the Factorial of a number.

n = input()
n = int(n)
fact = 1
for i in range(n):
  fact = fact*(i+1)
print(fact)
