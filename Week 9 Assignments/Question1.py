# Given a string, write a program to check if it is palindrome or not. A string is said to be a palindrome if the reverse of the string is the same as string.

def isPalindrome(s):
	return s == s[::-1]

s = input()
ans = isPalindrome(s)
 
if ans:
	print("YES")
else:
	print("NO")
