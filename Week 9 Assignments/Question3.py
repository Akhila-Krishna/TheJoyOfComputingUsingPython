// Let us assume paper as the plane and a letter as a curve on the plane, then each letter divides the plane into regions. 
// For example letters "A", "D", "O", "P", "R" divide the plane into two regions so we say these letters each have one hole. 
// Similarly, letter "B" has two holes and letters such as "C", "E", "F", "K" have no holes. 
// We say that the number of holes in the text is equal to the total number of holes in the letters of the text. 

// Write a program to determine how many holes are in a given text.

s = input()
holes = 0

h0 = ['C','E','F','G','H','I','J','K','L','M','N','S','T','U','V','W','X','Y','Z']
h1 = ['A','D','O','P','Q','R']
h2 = ['B']

for i in range(len(s)):
	if s[i] in h1:
		holes += 1
	elif s[i] in h2:
		holes += 2
	else:
		holes += 0

print(holes)
