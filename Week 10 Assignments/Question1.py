# You are provided with a number D containing only digits 0's and 1's. Your aim is to convert this number to have all the digits same.
# For that, you will change exactly one digit i.e. from 0 to 1 or from 1 to 0. 
# If it is possible to make all digits equal (either all 0's or all 1's) by flipping exactly 1 digit then output "YES", else print "NO" (quotes for clarity).

n = input()

c0 = 0
c1 = 0

for digit in str(n):
    digit = int(digit)
    if(digit == 0):
        c0 += 1
    else:
        c1 += 1

if(c0 == 1 or c1 == 1):
	  print("YES")
else:
	  print("NO")
