# With a given list L, write a program to print this list L after removing all duplicate values with original order reserved.

def Remove(duplicate): 
	final_list = [] 
	for num in duplicate: 
		if num not in final_list: 
			final_list.append(num)
	return final_list 

X = []
duplicate = []
duplicate = [int(item) for item in input().split()]
X = Remove(duplicate)
for a in X:
    print(a, end=" ")
