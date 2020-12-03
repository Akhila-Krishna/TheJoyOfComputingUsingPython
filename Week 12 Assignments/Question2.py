# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.


s = input()
count1 = 0
count2 = 0
for i in s:
	if(i.isupper()):
		count1 += 1
	elif(i.islower()):
		count2 += 1
print(count1, count2)
