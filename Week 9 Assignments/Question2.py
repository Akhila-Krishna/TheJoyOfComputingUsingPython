// Given a string S having characters from English alphabets ['a' - 'z'] and '.' as the special character (without quotes). 
// Write a program to construct the lexicographically smallest palindrome by filling each of the faded character ('.') with a lower case alphabet.

// Definition:
// The smallest lexicographical order is an order relation where string s is smaller than t, given the first character of s (s1 ) is smaller than the first character 
// of t (t1 ), or in case they are equivalent, the second character, etc.

def constructPalin(string, l): 
	string = list(string) 
	i = -1
	j = l 
	
	while i < j: 
		i += 1
		j -= 1

		if (string[i] == string[j] and
			string[i] != '.'): 
			continue
		elif (string[i] == string[j] and
			string[i] == '.'): 
			string[i] = 'a'
			string[j] = 'a'
			continue
		elif string[i] == '.': 
			string[i] = string[j] 
			continue
		elif string[j] == '.': 
			string[j] = string[i] 
			continue
		return -1 
	return ''.join(string) 

  
if __name__ == "__main__": 
	string = input()
	l = len(string) 
	print(constructPalin(string, l)) 
