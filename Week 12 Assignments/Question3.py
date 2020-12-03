# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. 
# Both user names and company names are composed of letters only.

start = '@'
end = '.'
s = input()
print((s.split(start))[1].split(end)[0])
